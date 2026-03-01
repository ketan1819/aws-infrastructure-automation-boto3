import boto3
from config.config import REGION, BUCKET_NAME

def create_s3_bucket():
    s3 = boto3.client("s3", region_name=REGION)

    response = s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            "LocationConstraint": REGION
        }
    )

    print(f"S3 Bucket '{BUCKET_NAME}' created successfully!")

if __name__ == "__main__":
    create_s3_bucket()