import boto3
from config.config import REGION, AMI_ID, INSTANCE_TYPE, KEY_PAIR_NAME

def launch_ec2():
    ec2 = boto3.resource("ec2", region_name=REGION)

    instances = ec2.create_instances(
        ImageId=AMI_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_PAIR_NAME
    )

    instance = instances[0]
    print(f"EC2 Instance Launched! Instance ID: {instance.id}")

if __name__ == "__main__":
    launch_ec2()