import json

def lambda_handler(event, context):
    # TODO implement done
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }