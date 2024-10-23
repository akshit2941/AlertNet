import json
import boto3
from botocore.exceptions import ClientError

# Initialize AWS clients
s3 = boto3.client('s3')
ses = boto3.client('ses')

def lambda_handler(event, context):
    # Extract sensor data from CloudWatch event
    magnitude = event['Records'][0]['Sns']['Message']
    bucket_name = 'disaster-event-logs'
    file_name = 'earthquake_log.json'
    
    # Log data in S3
    log_data = {
        'magnitude': magnitude,
        'time': event['Records'][0]['Sns']['Timestamp']
    }
    
    # Save log to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(log_data)
    )
    
    # Send notification email
    email_subject = "Disaster Alert: Earthquake Detected!"
    email_body = f"An earthquake of magnitude {magnitude} has been detected. Stay safe!"
    recipient_email = 'recipient@example.com'
    
    try:
        response = ses.send_email(
            Source='your-email@example.com',
            Destination={'ToAddresses': [recipient_email]},
            Message={
                'Subject': {'Data': email_subject},
                'Body': {'Text': {'Data': email_body}}
            }
        )
        print("Email sent!")
    except ClientError as e:
        print(f"Error sending email: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Alert sent successfully!')
    }
