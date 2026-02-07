import os
from datetime import date

# ================================
# Database Configuration
# ================================
DATABASE_NAME = "VEHICLE_INSURANCE"
COLLECTION_NAME = "VEHICLE_INSURANCE_DATA"
MONGODB_URL_KEY = "MONGODB_URL"

# ================================
# Pipeline & Artifacts
# ================================
PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

CURRENT_YEAR = date.today().year

# ================================
# Data Files
# ================================
FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

TARGET_COLUMN = "Response"

# ================================
# Preprocessing & Model Files
# ================================
MODEL_FILE_NAME = "model.pkl"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

# ================================
# Object Storage (Hugging Face)
# ================================
# Key names for environment variables (kept for reference, handled by object_storage_connection.py)
STORAGE_ACCESS_KEY_ENV = "STORAGE_ACCESS_KEY"
STORAGE_SECRET_KEY_ENV = "STORAGE_SECRET_KEY"
STORAGE_ENDPOINT_ENV = "STORAGE_ENDPOINT"
STORAGE_REGION_ENV = "STORAGE_REGION"

MODEL_REPO_ID = "learncode2025/vehicle-insurance-model" # Can also be read from env via HUGGINGFACE_REPO_ID
MODEL_REGISTRY_PATH = "model.pkl"

# ================================
# Data Ingestion
# ================================
DATA_INGESTION_COLLECTION_NAME: str = "VEHICLE_INSURANCE_DATA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

# ================================
# Data Validation
# ================================
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# ================================
# Data Transformation
# ================================
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# ================================
# Model Trainer
# ================================
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"

MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")

MODEL_TRAINER_N_ESTIMATORS: int = 200
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 6
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 10 
MIN_SAMPLES_SPLIT_CRITERION: str = 'entropy' 
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101

# ================================
# Model Evaluation
# ================================
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02

# ================================
# Application
# ================================
APP_HOST = "0.0.0.0"
APP_PORT = 5000
