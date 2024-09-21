# Bedrock
![alt text](https://github.com/CakeNuthep/bedrock/blob/main/image/Example.png)

## Require
Python 3.12.4

## Update .env File with AWS Credentials
update credentials in a file named .aws/credentials.
Do NOT commit the file to .git. The file should have content like this:
```
[default]
aws_access_key_id = XXXXXXXX
aws_secret_access_key = XXXXXXX
```

copy .aws folder to $home/.aws

## Installing Requirements
```sh
pip install -r requirements.txt
```

## Running Locally
```sh
streamlit run .\chatbot_frontend.py
```
