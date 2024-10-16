import os
import boto3
import logging
import requests
import time
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def call_request():
    """
    Call API for random users to getting multiple records to store into DynamoDB

    :return: return batch item with 100 of batches
    """
    url = "https://randomuser.me/api/?results=1"
    response = requests.get(url=url)
    result = [itr for itr in response.json()["results"]]
    return result


def write_data_into_table(resource=None):
    """
    Write data into the table.

    :param resource: Boto3 resource configuration
    :return: status code
    """
    if resource is None:
        resource = boto3.resource(
            "dynamodb",
            region_name=os.getenv("REGION_NAME", None),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", None),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", None)
        )

    table = resource.Table("RandomUser")
    with table.batch_writer() as writer:
        while True:
            for itr in call_request():
                writer.put_item(Item={**itr, "user_id": str(time.time())})

    logger.info("Data has been uploaded")
    table.wait_until_exists()
    return


if __name__ == "__main__":
    write_data_into_table()
