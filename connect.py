import boto3

AWS_ACCESS_KEY_ID="AKIAZ7TBUSG3OB3KGBN4"
AWS_SECRET_ACCESS_KEY="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"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)