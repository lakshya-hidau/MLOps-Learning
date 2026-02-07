#!/usr/bin/env python3
"""
Run the training pipeline with proper environment configuration.
Sets STORAGE_VERIFY=False to disable SSL certificate validation for custom endpoints.
"""
import os
import sys
from dotenv import load_dotenv

# Set environment variable to disable SSL verification for custom S3 endpoint
os.environ['STORAGE_VERIFY'] = 'False'

# Load environment variables from .env file
load_dotenv()

# Import and run the pipeline
from src.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
    print("\n" + "="*100)
    print("Pipeline execution completed successfully!")
    print("="*100)
