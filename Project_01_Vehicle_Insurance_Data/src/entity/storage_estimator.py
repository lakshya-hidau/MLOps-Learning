import sys
from pandas import DataFrame

from src.cloud_storage.object_storage import SimpleObjectStorageService
from src.exception import MyException
from src.entity.estimator import MyModel


class Proj1Estimator:
    """
    Handles model persistence and prediction using object storage.
    """

    def __init__(self, bucket_name: str, model_path: str):
        self.bucket_name = bucket_name
        self.model_path = model_path
        self.storage = SimpleObjectStorageService()
        self.model: MyModel = None

    def model_exists(self) -> bool:
        try:
            return self.storage.key_exists(self.bucket_name, self.model_path)
        except Exception:
            return False

    def load_model(self) -> MyModel:
        try:
            self.model = self.storage.load_pickle(
                filename=self.model_path,
                bucket_name=self.bucket_name,
            )
            return self.model
        except Exception as e:
            raise MyException(e, sys)

    def save_model(self, local_model_path: str, remove: bool = False):
        try:
            self.storage.upload_file(
                local_path=local_model_path,
                storage_path=self.model_path,
                bucket_name=self.bucket_name,
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
