# alb_lambda_project/lambda/hello.py
def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, world!'
    }
