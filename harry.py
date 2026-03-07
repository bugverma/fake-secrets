import boto3

AWS_ACCESS_KEY_ID="AKIA34UWIKTBTWQPHBZP"
AWS_SECRET_ACCESS_KEY="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"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)