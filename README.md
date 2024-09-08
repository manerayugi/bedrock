# Bedrock
![alt text](https://github.com/CakeNuthep/bedrock/blob/main/image/Example.png)

## Require
Python 3.12.4

## Update .env File with AWS Credentials
update credentials in a file named image/.env. Do NOT commit the file to .git. The file should have content like this:
```
AWS_ACCESS_KEY_ID=XXXXX
AWS_SECRET_ACCESS_KEY=XXXXX
AWS_DEFAULT_REGION=us-east-1
```

## Installing Requirements
```sh
pip install -r image/requirements.txt
```

## Running Locally
```sh
streamlit run .\chatbot_frontend.py
```
