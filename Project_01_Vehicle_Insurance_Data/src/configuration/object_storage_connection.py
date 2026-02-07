import os
import logging
from dotenv import load_dotenv
from huggingface_hub import HfApi

# Load environment variables from .env file
load_dotenv()

class ObjectStorageClient:
    api = None
    repo_id = None
    repo_type = None

    def __init__(self):
        if ObjectStorageClient.api is None:
            token = os.getenv("HUGGINGFACE_TOKEN")
            repo_id = os.getenv("HUGGINGFACE_REPO_ID")
            repo_type = os.getenv("HUGGINGFACE_REPO_TYPE", "model")

            if not token or not repo_id:
                raise Exception("Hugging Face credentials (token, repo_id) are not set in environment variables.")

            ObjectStorageClient.api = HfApi(token=token)
            ObjectStorageClient.repo_id = repo_id
            ObjectStorageClient.repo_type = repo_type

        self.api = ObjectStorageClient.api
        self.repo_id = ObjectStorageClient.repo_id
        self.repo_type = ObjectStorageClient.repo_type
