import json

def lambda_handler(event, context):
    # TODO implementation done
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
