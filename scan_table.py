import os
import boto3
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def scan_table(resource=None):
    """
    Scan full table into DynamoDB.

    :param resource: Boto3 resource configuration
    :return: full table columns
    """
    if resource is None:
        resource = boto3.resource(
            "dynamodb",
            region_name=os.getenv("REGION_NAME", None),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", None),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", None)
        )

    table_name = resource.Table("RandomUser")
    response = table_name.scan()
    return response["Items"]


if __name__ == "__main__":
    num_of_rows = len(scan_table())
    logger.error(f"Scaning completed... number of rows: {num_of_rows}")
