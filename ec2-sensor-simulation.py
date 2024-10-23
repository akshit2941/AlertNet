import random
import time
import boto3

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch')

def generate_earthquake_data():
    # Random earthquake magnitude between 4.0 and 8.0
    magnitude = round(random.uniform(4.0, 8.0), 2)
    return magnitude

def push_data_to_cloudwatch(magnitude):
    response = cloudwatch.put_metric_data(
        Namespace='DisasterMonitoring',
        MetricData=[
            {
                'MetricName': 'EarthquakeMagnitude',
                'Unit': 'None',
                'Value': magnitude
            }
        ]
    )
    print(f'Data sent to CloudWatch: {magnitude}')

def main():
    while True:
        magnitude = generate_earthquake_data()
        push_data_to_cloudwatch(magnitude)
        time.sleep(60)  # Push data every minute

if __name__ == '__main__':
    main()
