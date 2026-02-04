import os
import sys
import pickle
from io import StringIO
from typing import Union, List

from pandas import DataFrame, read_csv
from botocore.exceptions import ClientError

from src.configuration.object_storage_connection import ObjectStorageClient
from src.exception import MyException
from src.logger import logging


class SimpleObjectStorageService:
    """
    Object storage service for file upload, download, and data retrieval.
    """

    def __init__(self):
        client = ObjectStorageClient()
        self.storage_resource = client.resource
        self.storage_client = client.client

    def get_bucket(self, bucket_name: str):
        try:
            return self.storage_resource.Bucket(bucket_name)
        except Exception as e:
            raise MyException(e, sys)

    def key_exists(self, bucket_name: str, key: str) -> bool:
        try:
            bucket = self.get_bucket(bucket_name)
            return len(list(bucket.objects.filter(Prefix=key))) > 0
        except Exception as e:
            raise MyException(e, sys)

    def get_file_object(self, filename: str, bucket_name: str):
        try:
            bucket = self.get_bucket(bucket_name)
            objects = list(bucket.objects.filter(Prefix=filename))
            return objects[0] if len(objects) == 1 else objects
        except Exception as e:
            raise MyException(e, sys)

    @staticmethod
    def read_object(obj, decode: bool = True, readable: bool = False):
        try:
            data = obj.get()["Body"].read()
            if decode:
                data = data.decode()
            return StringIO(data) if readable else data
        except Exception as e:
            raise MyException(e, sys)

    def upload_file(self, local_path: str, storage_path: str, bucket_name: str, remove: bool = False):
        try:
            logging.info(f"Uploading {local_path} → {bucket_name}/{storage_path}")
            self.storage_client.upload_file(local_path, bucket_name, storage_path)

            if remove:
                os.remove(local_path)
        except Exception as e:
            raise MyException(e, sys)

    def upload_dataframe_as_csv(
        self,
        dataframe: DataFrame,
        local_filename: str,
        bucket_filename: str,
        bucket_name: str,
    ):
        try:
            dataframe.to_csv(local_filename, index=False)
            self.upload_file(local_filename, bucket_filename, bucket_name, remove=True)
        except Exception as e:
            raise MyException(e, sys)

    def read_csv(self, filename: str, bucket_name: str) -> DataFrame:
        try:
            obj = self.get_file_object(filename, bucket_name)
            content = self.read_object(obj, readable=True)
            return read_csv(content)
        except Exception as e:
            raise MyException(e, sys)

    def load_pickle(self, filename: str, bucket_name: str):
        try:
            obj = self.get_file_object(filename, bucket_name)
            binary = self.read_object(obj, decode=False)
            return pickle.loads(binary)
        except Exception as e:
            raise MyException(e, sys)

    def create_folder(self, folder_name: str, bucket_name: str):
        try:
            self.storage_resource.Object(bucket_name, folder_name + "/").load()
        except ClientError:
            self.storage_client.put_object(
                Bucket=bucket_name,
                Key=f"{folder_name}/"
            )
