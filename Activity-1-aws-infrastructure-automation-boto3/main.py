from s3.create_bucket import create_s3_bucket
from ec2.launch_instance import launch_ec2
from vpc.create_vpc import create_vpc
from iam.create_role import create_iam_role

def main():
    print("Starting AWS Infrastructure Automation...\n")

    create_s3_bucket()
    create_vpc()
    launch_ec2()
    create_iam_role()

    print("\nAll Resources Created Successfully!")

if __name__ == "__main__":
    main()