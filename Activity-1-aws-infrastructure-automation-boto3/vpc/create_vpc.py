import boto3
from config.config import REGION

def create_vpc():
    ec2 = boto3.client("ec2", region_name=REGION)

    response = ec2.create_vpc(
        CidrBlock="10.0.0.0/16"
    )

    vpc_id = response["Vpc"]["VpcId"]

    print(f"VPC Created Successfully! VPC ID: {vpc_id}")

if __name__ == "__main__":
    create_vpc()