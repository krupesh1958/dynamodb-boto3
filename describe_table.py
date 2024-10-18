import os
import boto3
from pprint import pprint


resource = boto3.client(
    "dynamodb",
    region_name=os.getenv("REGION_NAME", None),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", None),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", None)
)


def describe_table(table_name):
    response = resource.describe_table(TableName=table_name)
    return response


pprint(describe_table("RandomUser"))
