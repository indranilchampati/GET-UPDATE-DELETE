import json
import boto3


dynamodb_client = boto3.client('dynamodb')

# set table
customer_table = 'customer'
product_table = 'product'
address_table = 'address'
order_table = 'order'


def lambda_handler(event, context):

    key = {'customer_id': {'S': '1'}}

# delete
    resp = dynamodb_client.get_item(
        TableName=customer_table,
        Key=key)

# print response
    print(resp['Item'])
    return resp
