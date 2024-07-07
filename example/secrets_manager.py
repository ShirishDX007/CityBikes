import boto3
import json

def get_secret(secret_name):

    secret_name = "AWS_ses_east_new"
    region_name = "us-east-1"
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)
