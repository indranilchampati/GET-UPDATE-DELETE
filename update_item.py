import boto3

# client for dynamoDB
dynamodb_client = boto3.client('dynamodb')

# set table
customer_table = 'customer'
product_table = 'product'
address_table = 'address'
order_table = 'order'


'''
get item from product_table
'''
# need to set a key to elete
key = {
    'product_id': {'S': '1'}
}

response = dynamodb_client.update_item(
    TableName=product_table,
    Key=key,
    ExpressionAttributeNames={
        '#st': 'stock'
    },
    UpdateExpression="set #st = :count",
    ExpressionAttributeValues={
        ':count': {
            'N': '10'
        }
    }
)


# print response
print(response)
