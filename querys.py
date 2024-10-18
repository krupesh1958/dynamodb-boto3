import os
import boto3
import logging
from dotenv import load_dotenv
import typing as t


load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

DictValue = t.Dict[str, t.Dict[str, str]]

resource = boto3.client(
    "dynamodb",
    region_name=os.getenv("REGION_NAME", None),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", None),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", None)
)


def query_on_the_primary_index(
    user_id: str,
    email: str,
    resource = None
) -> t.List[DictValue]:
    """
    Query on the primary index.

    :param user_id: Boto3 resource configuration
    :return: items from the table
    """
    response = resource.query(
        TableName="RandomUser",
        KeyConditionExpression="user_id = :user_id AND email = :email",
        ExpressionAttributeValues={
            ":user_id": {"S": user_id},
            ":email": {"S": email}
        }
    )
    return response.get("Items", [])


# logger.error(
#     "Items from the table: %s",
#     query_on_the_primary_index("1729245542.589026", "diy.hudenko@example.com")
# )


def query_on_the_secondary_index(
    user_id: str,
    dob: str,
    resource = None
) -> t.List[DictValue]:
    """
    Query on the secondary index.

    :param user_id: Boto3 resource configuration
    :return: items from the table
    """
    response = resource.query(
        TableName="RandomUser",
        KeyConditionExpression="user_id = :user_id",
        ExpressionAttributeValues={
            ":user_id": {"S": user_id}
        }
    )
    return response.get("Items", [])

# logger.error(
#     "Items from the table: %s",
#     query_on_the_secondary_index("1729245542.589026", "1729245542.589031")
# )


def scan_whole_table_with_pagination():
    scan_kwargs = {}
    items = []

    while True:
        response = resource.scan(
            TableName="RandomUser",
            **scan_kwargs
        )
        items.extend(response.get("Items", []))

        try:
            scan_kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]
        except KeyError:
            break
    return items


# logger.error("Items from the table: %s", len(scan_table_with_pagination()))
