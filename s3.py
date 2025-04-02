import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch credentials and region from the environment
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

# Upload file to S3
def upload_to_s3(file_obj, bucket_name, s3_file_name):
    # Initialize the S3 client with credentials and region
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    try:
        # Upload the file-like object (in-memory PDF) to the specified S3 bucket
        s3.upload_fileobj(file_obj, bucket_name, s3_file_name)
        print(f"File uploaded to S3 bucket '{bucket_name}' as '{s3_file_name}'")
    except FileNotFoundError:
        print(f"File '{file_obj}' not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"An error occurred: {e}")
