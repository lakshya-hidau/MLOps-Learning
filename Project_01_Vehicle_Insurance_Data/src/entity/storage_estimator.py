import sys
from pandas import DataFrame

from src.cloud_storage.object_storage import SimpleObjectStorageService
from src.exception import MyException
from src.entity.estimator import MyModel


class Proj1Estimator:
    """
    Handles model persistence and prediction using object storage.
    """

    def __init__(self, repo_id: str, model_path: str):
        self.repo_id = repo_id
        self.model_path = model_path
        self.storage = SimpleObjectStorageService()
        self.model: MyModel = None

    def is_model_exists(self, model_path: str = None) -> bool:
        """
        Check if model exists in the storage. If `model_path` is not provided,
        the instance's `self.model_path` will be used.
        """
        try:
            path_to_check = self.model_path if model_path is None else model_path
            return self.storage.key_exists(self.repo_id, path_to_check)
        except Exception:
            return False

    # backward compatibility alias
    def is_model_present(self, model_path: str = None) -> bool:
        return self.is_model_exists(model_path)

    def load_model(self) -> MyModel:
        try:
            self.model = self.storage.load_pickle(
                filename=self.model_path,
                repo_id=self.repo_id,
            )
            return self.model
        except Exception as e:
            raise MyException(e, sys)

    def save_model(self, local_model_path: str = None, from_file: str = None, remove: bool = False):
        """
        Upload a local model file to storage. Supports both positional `local_model_path`
        and keyword `from_file` for backward compatibility with existing callers.
        """
        try:
            path_to_upload = from_file if from_file is not None else local_model_path
            if path_to_upload is None:
                raise ValueError("Either 'local_model_path' or 'from_file' must be provided")

            self.storage.upload_file(
                local_path=path_to_upload,
                storage_path=self.model_path,
                repo_id=self.repo_id,
                remove=remove,
            )
        except Exception as e:
            raise MyException(e, sys)

    def predict(self, dataframe: DataFrame):
        try:
            if self.model is None:
                self.load_model()
            return self.model.predict(dataframe=dataframe)
        except Exception as e:
            raise MyException(e, sys)
