import boto3
import json

def get_secret(secret_name):
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)
