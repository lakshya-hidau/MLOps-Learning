import boto3
import os

class ObjectStorageClient:
    client = None
    resource = None

    def __init__(self):
        if ObjectStorageClient.client is None or ObjectStorageClient.resource is None:
            access_key = os.getenv("STORAGE_ACCESS_KEY")
            secret_key = os.getenv("STORAGE_SECRET_KEY")
            endpoint = os.getenv("STORAGE_ENDPOINT")
            region = os.getenv("STORAGE_REGION", "us-east-1")

            if not access_key or not secret_key or not endpoint:
                raise Exception("Object storage credentials are not set")

            ObjectStorageClient.resource = boto3.resource(
                "s3",
                endpoint_url=endpoint,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region,
            )

            ObjectStorageClient.client = boto3.client(
                "s3",
                endpoint_url=endpoint,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region,
            )

        self.resource = ObjectStorageClient.resource
        self.client = ObjectStorageClient.client
