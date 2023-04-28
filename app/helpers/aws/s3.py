
### Upload to s3 ###

import base64
import boto3
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Load env variables
AWS_KEY = str(os.environ.get("AWS_KEY", "error_key"))
AWS_ACCESS_KEY = str(os.environ.get("AWS_ACCESS_KEY", "error_key"))


async def upload_image_s3(image_base64: str):
    image_data = base64.b64decode(image_base64)

    S3 = boto3.client('s3',
                      aws_access_key_id=AWS_KEY,
                      aws_secret_access_key=AWS_ACCESS_KEY
                      )

    BUCKET_NAME = 'your-bucket-name'
    FILE_NAME = 'your-image-file-name.jpg'

    UPLOAD = S3.put_object(
        Body=image_data,
        Bucket=BUCKET_NAME,
        Key=FILE_NAME)

    print(UPLOAD)
