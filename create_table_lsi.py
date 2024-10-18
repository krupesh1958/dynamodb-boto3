import os
import boto3
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def create_table_lsi(resource=None):
    """
    Creates a DynamoDB table with a Local Secondary Index.

    :param resource: Boto3 resource configuration
    :return: The newly created table.
    """
    if resource is None:
        resource = boto3.resource(
            "dynamodb",
            region_name=os.getenv("REGION_NAME", None),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", None),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", None)
        )

    table_name = "RandomUser"
    params = {
        "TableName": table_name,
        "KeySchema": [
            {"AttributeName": "user_id", "KeyType": "HASH"},
            {"AttributeName": "email", "KeyType": "RANGE"}
        ],
        "AttributeDefinitions": [
            {"AttributeName": "user_id", "AttributeType": "S"},
            {"AttributeName": "email", "AttributeType": "S"},
            {"AttributeName": "dob", "AttributeType": "S"}
        ],
        "LocalSecondaryIndexes": [
            {
                "IndexName": "DateOfBirthIndex",
                "KeySchema": [
                    {"AttributeName": "user_id", "KeyType": "HASH"},
                    {"AttributeName": "dob", "KeyType": "RANGE"}
                ],
                "Projection": {"ProjectionType": "ALL"}
            }
        ],
        "ProvisionedThroughput": {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    }
    table = resource.create_table(**params)
    logger.info(f"Creating {table_name}...")
    table.wait_until_exists()
    return table


if __name__ == "__main__":
    create_table_lsi()
    print("Created table with Local Secondary Index...")
