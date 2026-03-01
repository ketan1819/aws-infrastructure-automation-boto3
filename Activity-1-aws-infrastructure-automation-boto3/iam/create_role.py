import boto3
import json
from config.config import REGION

def create_iam_role():
    iam = boto3.client("iam", region_name=REGION)

    assume_role_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"Service": "ec2.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
        ]
    }

    response = iam.create_role(
        RoleName="EC2-S3-Access-Role",
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )

    print("IAM Role Created Successfully!")

if __name__ == "__main__":
    create_iam_role()