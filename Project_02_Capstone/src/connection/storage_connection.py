import pandas as pd
import logging
from io import StringIO
from huggingface_hub import hf_hub_download
from src.logger import logging


class hf_storage_operations:
    def __init__(self, repo_id, token=None, repo_type="dataset"):
        """
        Initialize Hugging Face storage operations.
        
        :param repo_id: Hugging Face repo id (e.g., 'learncode2025/MLOps-Learning_Project_02_Capstone')
        :param token: Hugging Face access token (optional for private repos)
        :param repo_type: 'dataset' or 'model'
        """
        self.repo_id = repo_id
        self.token = token
        self.repo_type = repo_type
        logging.info("Data Ingestion from Hugging Face storage initialized")

    def fetch_file_from_hf(self, file_path):
        """
        Fetches a CSV file from Hugging Face Dataset repo and returns it as a Pandas DataFrame.
        
        :param file_path: Path inside HF repo (e.g., 'data/data.csv')
        :return: Pandas DataFrame
        """
        try:
            logging.info(f"Fetching file '{file_path}' from Hugging Face repo '{self.repo_id}'...")

            # Download file from Hugging Face repo
            local_file_path = hf_hub_download(
                repo_id=self.repo_id,
                filename=file_path,
                repo_type=self.repo_type,
                token=self.token  # Required if repo is private
            )

            # Load CSV into pandas
            df = pd.read_csv(local_file_path)

            logging.info(
                f"Successfully fetched and loaded '{file_path}' from Hugging Face with {len(df)} records."
            )
            return df

        except Exception as e:
            logging.exception(f"❌ Failed to fetch '{file_path}' from Hugging Face: {e}")
            return None


# Example usage
# if __name__ == "__main__":
#     REPO_ID = "<hf_username>/<repo_name>"
#     HF_TOKEN = "<hf_token>"  # Needed if private repo
#     FILE_PATH = "<file_path>"  # Path inside HF dataset repo

#     data_ingestion = hf_storage_operations(
#         repo_id=REPO_ID,
#         token=HF_TOKEN
#     )

#     df = data_ingestion.fetch_file_from_hf(FILE_PATH)

#     if df is not None:
#         print(f"Data fetched with {len(df)} records.")