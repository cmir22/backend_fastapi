
### Upload to s3 ###

import boto3
from dotenv import load_dotenv
import os
import base64
from helpers.aws.buckets import COFFFEE_FINDER_BUCKET
import uuid


# Load .env
load_dotenv()

# Load env variables
ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


def upload_image_s3(image_base64: str, id_business: str):
    uuid_obj = str(uuid.uuid4())[:13]
    custom_name = ""
    print(uuid_obj)

    # try:

    #     S3_CLIENT = boto3.client('s3',
    #                              aws_access_key_id=ACCESS_KEY,
    #                              aws_secret_access_key=SECRET_ACCESS_KEY)

    #     # Decode the base64 image
    #     IMAGE_DATA = base64.b64decode(image_base64)

    #     S3_CLIENT.put_object(Body=IMAGE_DATA,
    #                          Bucket=COFFFEE_FINDER_BUCKET,
    #                          Key="SIUUU.jpeg")

    # except Exception as exs:
    #     print(exs)
