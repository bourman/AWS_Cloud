import json
import boto3

def lambda_handler(event, context):
    num1 = float(event['num1'])
    num2 = float(event['num2'])
    result = num1 + num2
    sns = boto3.client('sns')
    message = f"The sum of {num1} and {num2} is {result}"
    topic_arn = 'arn:aws:sns:us-east-2:756212760270:dem'
    response = sns.publish(TopicArn=topic_arn, Message=message)
    return response
