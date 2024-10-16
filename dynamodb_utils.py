"""Filter the attributes type of a DynamoDB table."""


def transform_dynmaodb_response(item):
    """Remove the type of attributes from the DynamoDB response."""
    if isinstance(item, dict):
        if "S" in item:
            return item["S"]
        elif "N" in item:
            return int(item["N"]) if item["N"].isdigit() else float(item["N"])
        elif "M" in item:
            return {key: transform_dynmaodb_response(value) for key, value in item["M"].items()}
        else:
            return {key: transform_dynmaodb_response(value) for key, value in item.items()}
    elif isinstance(item, list):
        return [transform_dynmaodb_response(value) for value in item]
    else:
        return item


def filter_attributes_types(attributes):
    """
    Filter the attributes type of a DynamoDB table.

    :param attributes: attributes from the table
    :return: filtered attributes
    """
    for item in attributes:
        yield transform_dynmaodb_response(item)
