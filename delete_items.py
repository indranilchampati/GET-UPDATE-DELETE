import boto3 

# client for dynamoDB 
dynamodb_client = boto3.client('dynamodb')

# set table 
customer_table = 'customer'
product_table = 'product'
address_table = 'address'
order_table = 'order'

'''
Delete from product_table
'''
# need to set a key to elete 
key ={
    'product_id':{'S':'4'}
}

# delete
resp = dynamodb_client.delete_item(
    TableName = product_table,
    Key = key)
    
# print response 
print(resp)