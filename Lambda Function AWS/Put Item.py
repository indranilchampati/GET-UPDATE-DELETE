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

    item = {'customer_id': {'S': '1'}, 'first-name': {'S': 'Indranil'},
            'last-name': {'S': 'Champati'}}

# put item into dynamo
    resp = dynamodb_client.put_item(
        TableName=customer_table,
        Item=item)


# item for table
    item = {
        'customer_id': {'S': '2'}, 'first-name': {'S': 'Siddhart'}, 'last-name': {'S': 'Porval'}
    }
# put item into dynamo
    resp = dynamodb_client.put_item(
        TableName=customer_table,
        Item=item)
# item for table
    item = {
        'customer_id': {'S': '3'}, 'first-name': {'S': 'Manali'}, 'last-name': {'S': 'Jain'}
    }

# put item into dynamo
    resp = dynamodb_client.put_item(
        TableName=customer_table,
        Item=item)

    item = {'product_id': {'S': '1'}, 'description': {
        'S': 'Ipad'}, 'stock': {'N': '5'}}
    resp = dynamodb_client.put_item(TableName=product_table, Item=item)

    item = {'product_id': {'S': '2'}, 'description': {
        'S': 'Iphone'}, 'stock': {'N': '5'}}
    resp = dynamodb_client.put_item(TableName=product_table, Item=item)

    item = {'product_id': {'S': '3'}, 'description': {
        'S': 'mac'}, 'stock': {'N': '5'}}

# put item into dynamo
    resp = dynamodb_client.put_item(TableName=product_table, Item=item)

# item for table
    item = {'product_id': {'S': '4'}, 'description': {
        'S': 'Air Pods'}, 'stock': {'N': '5'}}

# put item into dynamo
    resp = dynamodb_client.put_item(TableName=product_table, Item=item)
    item = {'address_id': {'S': '1'}, 'customer_id': {
        'S': '1'}, 'street': {'S': '123 made up st'}}
# put item into dynamo
    resp = dynamodb_client.put_item(TableName=address_table, Item=item)
# item for table
    item = {'address_id': {'S': '4'}, 'customer_id': {
        'S': '1'}, 'street': {'S': '123 shipping st'}}
# put item into dynamo
    resp = dynamodb_client.put_item(TableName=address_table, Item=item)
# item for table
    item = {'address_id': {'S': '2'}, 'customer_id': {
        'S': '2'}, 'street': {'S': '456 no where land'}}
# put item into dynamo
    resp = dynamodb_client.put_item(TableName=address_table, Item=item)
# item for table
    item = {'address_id': {'S': '3'}, 'customer_id': {
        'S': '3'}, 'street': {'S': '78 near the port'}}
# put item into dynamo
    resp = dynamodb_client.put_item(TableName=address_table, Item=item)
    return resp


# item for table
