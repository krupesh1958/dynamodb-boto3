import os
import boto3
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_items_from_table(resource=None):
    """
    Get items from the table.

    :param resource: Boto3 resource configuration
    :return: items from the table
    """
    if resource is None:
        resource = boto3.client(
            "dynamodb",
            region_name=os.getenv("REGION_NAME", None),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", None),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", None)
        )

    response = resource.batch_get_item(
        RequestItems={
            "RandomUser": {
                "Keys": [
                    {
                        "user_id": {"S": "1729054663.159515"},
                        "email": {"S": "angel.lozano@example.com"}
                    },
                ]
            }
        }
    )
    from dynamodb_utils import filter_attributes_types as filter_attributes
    return [itr for itr in filter_attributes(response.get("Responses", {}).get("RandomUser", []))]

logger.error("Items from the table: %s", get_items_from_table())
