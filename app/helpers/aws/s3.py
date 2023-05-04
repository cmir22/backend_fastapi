
### Upload to s3 ###

import boto3
from dotenv import load_dotenv
import os
import base64
from helpers.aws.buckets import COFFFEE_FINDER_BUCKET
import uuid
from PIL import Image
import io


# Load .env
load_dotenv()

# Load env variables
ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


def upload_image_s3(image_base64: str, id_business: str, section: str):
    IMAGE_FORMAT = "webp"

    try:
        CUSTOM_UUID = str(uuid.uuid4())
        CUSTOM_KEY_PATH = f"images/{id_business}/{section}/{CUSTOM_UUID}.{IMAGE_FORMAT}"

        ACL = 'public-read'

        # Decode the base64 image
        image_bytes = base64.b64decode(image_base64.split(',')[1])
        new_image = Image.open(io.BytesIO(image_bytes))

        # Convert image to webp
        with io.BytesIO() as output:
            new_image.save(output, format='WebP')
            WEBP_DATA = output.getvalue()

        # Create connection with AWS S3
        S3_CLIENT = boto3.client('s3',
                                 aws_access_key_id=ACCESS_KEY,
                                 aws_secret_access_key=SECRET_ACCESS_KEY)

        NEW_URL = generate_presigned_url(S3_CLIENT, CUSTOM_KEY_PATH)

        # Upload Object to S3
        STATUS = S3_CLIENT.put_object(Body=WEBP_DATA,
                                      Bucket=COFFFEE_FINDER_BUCKET,
                                      Key=CUSTOM_KEY_PATH,
                                      ContentType=f'image/{IMAGE_FORMAT}',
                                      ACL=ACL)

        return validate_reponse(STATUS, NEW_URL)

    except Exception as exs:
        print(exs)


def generate_presigned_url(S3_CLIENT, CUSTOM_KEY_PATH):
    PARAMS = {"Bucket": COFFFEE_FINDER_BUCKET, "Key": CUSTOM_KEY_PATH}
    METHOD = 'put_object'

    # GENERATE PRESIGNED URL
    URL = S3_CLIENT.generate_presigned_url(ClientMethod=METHOD,
                                           Params=PARAMS)
    # TRIM QUERY PARAMS
    NEW_URL = URL[0: URL.index('?')]

    return NEW_URL


def validate_reponse(STATUS, NEW_URL):
    response = {}
    STATUS = STATUS["ResponseMetadata"]["HTTPStatusCode"]

    if STATUS == 200:
        response = {
            "success": True,
            "inserted_url": NEW_URL
        }
    else:
        response = {
            "success": False,
        }

    return response
