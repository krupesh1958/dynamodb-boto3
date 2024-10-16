# DynamoDB with Boto3

This project demonstrates how to interact with Amazon DynamoDB using the Boto3 library in Python.

## Prerequisites

- Python 3.x
- Boto3 library
- AWS account with DynamoDB access

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dynamodb-boto3.git
    cd dynamodb-boto3
    ```

2. Install the required packages:
    ```sh
    pip install boto3
    ```

## Configuration

Ensure you have your AWS credentials configured. You can set them up using the AWS CLI:
```sh
aws configure
```

## Usage

### Creating a Table

To create a DynamoDB table, run:
```sh
python create_table.py
```

### Inserting Data

To insert data into the table, run:
```sh
python insert_data.py
```

### Querying Data

To query data from the table, run:
```sh
python query_data.py
```
