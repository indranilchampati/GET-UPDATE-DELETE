import json
import boto3

# client for dynamoDB
dynamodb_client = boto3.client('dynamodb')

# set table
customer_table = 'customer'
product_table = 'product'
address_table = 'address'
order_table = 'order'


def lambda_handler(event, context):
    # TODO implement
    key = {'product_id': {'S': '4'}}
    resp = dynamodb_client.delete_item(
        TableName=product_table,
        Key=key)
    print(resp)
    return resp
