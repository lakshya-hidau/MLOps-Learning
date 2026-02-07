import os
import sys
import pickle
from io import StringIO, BytesIO
from typing import Union, List

from pandas import DataFrame, read_csv
from huggingface_hub import hf_hub_download
from huggingface_hub.utils import RepositoryNotFoundError, RevisionNotFoundError, EntryNotFoundError

from src.configuration.object_storage_connection import ObjectStorageClient
from src.exception import MyException
from src.logger import logging

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SimpleObjectStorageService:
    """
    Object storage service for file upload, download, and data retrieval using Hugging Face Hub.
    """

    def __init__(self):
        client = ObjectStorageClient()
        self.api = client.api
        self.repo_id = client.repo_id
        self.repo_type = client.repo_type

    def key_exists(self, repo_id: str, key: str) -> bool:
        """
        Check if a file exists in the HF repository.
        'bucket_name' is ignored as repo_id is used from env.
        'key' is the path to the file in the repo.
        """
        try:
            # List repo files to check existence. 
            # Ideally use api.file_exists but list_repo_files is robust.
            files = self.api.list_repo_files(repo_id=self.repo_id, repo_type=self.repo_type)
            return key in files
        except Exception as e:
            # If repo doesn't exist or other error
            logging.error(f"Error checking key existence: {e}")
            return False

    def get_file_object(self, filename: str, repo_id: str):
        """
        Downloads the file from HF Hub and returns the local path.
        In this implementation, it returns the local path to the downloaded file.
        bucket_name is ignored.
        """
        try:
            local_path = hf_hub_download(
                repo_id=self.repo_id,
                filename=filename,
                repo_type=self.repo_type
            )
            return local_path
        except (RepositoryNotFoundError, RevisionNotFoundError, EntryNotFoundError) as e:
            raise Exception(f"File '{filename}' not found in repo '{self.repo_id}': {e}")
        except Exception as e:
            raise MyException(e, sys)

    @staticmethod
    def read_object(obj, decode: bool = True, readable: bool = False):
        """
        Reads the content from the local file path returned by get_file_object.
        """
        try:
            # obj is the local file path
            with open(obj, 'rb') as f:
                data = f.read()
            
            if decode:
                data = data.decode()
            
            return StringIO(data) if readable else data
        except Exception as e:
            raise MyException(e, sys)

    def upload_file(self, local_path: str, storage_path: str, repo_id: str, remove: bool = False):
        """
        Uploads a file to the HF repository.
        """
        try:
            logging.info(f"Uploading {local_path} → {self.repo_id}/{storage_path}")
            
            self.api.upload_file(
                path_or_fileobj=local_path,
                path_in_repo=storage_path,
                repo_id=self.repo_id,
                repo_type=self.repo_type
            )

            if remove:
                os.remove(local_path)
            
            logging.info(f"Upload successful: {storage_path}")
        except Exception as e:
            raise MyException(e, sys)

    def upload_dataframe_as_csv(
        self,
        dataframe: DataFrame,
        local_filename: str,
        bucket_filename: str,
        repo_id: str,
    ):
        try:
            dataframe.to_csv(local_filename, index=False)
            self.upload_file(local_filename, bucket_filename, repo_id, remove=True)
        except Exception as e:
            raise MyException(e, sys)

    def read_csv(self, filename: str, repo_id: str) -> DataFrame:
        try:
            # Download file
            local_path = self.get_file_object(filename, repo_id)
            return read_csv(local_path)
        except Exception as e:
            raise MyException(e, sys)

    def load_pickle(self, filename: str, repo_id: str):
        try:
            local_path = self.get_file_object(filename, repo_id)
            with open(local_path, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            raise MyException(e, sys)

    def create_folder(self, folder_name: str, repo_id: str):
        # HF doesn't have explicit folders, they are created by path.
        # We can create a .gitkeep or similar if strictly needed, but usually not required.
        pass
