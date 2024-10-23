# Disaster Response and Management System

## Overview
This project is a Disaster Response and Management System using AWS services to monitor, detect, and notify users about natural disasters such as earthquakes, floods, hurricanes, and heavy rainfall. It uses an EC2 instance to simulate IoT sensor data, CloudWatch for real-time monitoring, AWS Lambda to process data and trigger alerts, SES (Simple Email Service) to send email notifications, and S3 to store disaster-related data for future analysis.

Additionally, a web platform allows users to report nearby disasters like landslides and notifies others in the affected area. The system is scalable and can be extended to support various disaster types and notification channels.

## Architecture Overview
- **EC2 (IoT Simulation)**: Simulates disaster metrics like earthquake magnitude, water levels, etc.
- **CloudWatch**: Monitors EC2 data and triggers alarms when thresholds are breached.
- **AWS Lambda**: Processes alarm triggers and sends notifications via SES, and stores event data in S3.
- **Amazon S3**: Stores historical disaster event data for research purposes.
- **Amazon SNS (Optional)**: Could be used for SMS/push notifications in addition to emails.
- **Website**: Allows users to report nearby disasters like landslides, with the ability to notify others.

## Features
- Real-time disaster monitoring using IoT simulation (EC2).
- CloudWatch monitoring with alarm-based triggers.
- Automated email notifications via SES when disaster thresholds are exceeded.
- Event data storage in S3 for future analysis.
- User-submitted disaster reports (like landslides) via a web interface.

## Services Used
- **Amazon EC2**: Simulating IoT data.
- **Amazon CloudWatch**: Monitoring and setting alarms.
- **AWS Lambda**: Processing CloudWatch alarms and triggering actions.
- **Amazon SES**: Sending email notifications to users.
- **Amazon S3**: Storing disaster data for research and future analysis.

## Getting Started

### Prerequisites
To set up this project, you will need the following:
- AWS Account
- Basic knowledge of AWS services (EC2, CloudWatch, Lambda, SES, S3)
- GitHub repository to store your project
- Node.js (if using for backend)
- Python (if using for scripting)

### Steps to Deploy the System

1. **Set up EC2 instance**:
   - Launch an EC2 instance and configure it to simulate IoT sensor data.
   - Use a Python script to generate data for earthquake magnitudes, water levels, etc.

2. **Set up CloudWatch**:
   - Use CloudWatch to monitor the EC2 instance metrics and set alarms for specific thresholds (e.g., earthquake magnitude > 6.5).

3. **Lambda Function**:
   - Create a Lambda function that will be triggered by CloudWatch alarms.
   - The function processes sensor data and sends email alerts using AWS SES.

4. **S3 for Data Storage**:
   - Set up an S3 bucket to store event logs and IoT sensor data.

5. **SES for Notifications**:
   - Set up SES to send notifications to users when disasters are detected.

6. **Website**:
   - Deploy a website where users can report disasters like landslides. Integrate this with your AWS Lambda and S3 services to handle user reports.

7. **Testing and Verification**:
   - Test the end-to-end flow by simulating disaster data, triggering alarms, and ensuring notifications are sent.

## Files in this Repository

1. **EC2 Script**: `ec2-sensor-simulation.py`
   - Simulates IoT sensor data for disasters like earthquakes, floods, etc.

2. **Lambda Function**: `lambda-alert-handler.py`
   - Handles CloudWatch alarms, processes disaster data, sends email alerts, and stores logs in S3.

3. **Website Code**: `website/`
   - Includes frontend and backend code to allow users to report disasters.

4. **CloudFormation**: `cloudformation-template.yaml`
   - Optionally, an AWS CloudFormation template to automate the creation of the resources (EC2, Lambda, S3, SES, etc.).

## Usage

1. **Simulating IoT Data**:
   - SSH into the EC2 instance and run the Python script to generate sensor data.
   - Data will be sent to CloudWatch for monitoring.

2. **Monitoring and Triggering Alerts**:
   - CloudWatch continuously monitors incoming data and triggers an alarm if any thresholds (e.g., earthquake > 6.5) are breached.
   - Lambda function is invoked to handle the alarm and take the necessary actions.

3. **Email Notifications**:
   - AWS SES sends real-time email notifications to users when an event is triggered.

4. **User-Submitted Disasters**:
   - Users can report nearby disasters like landslides through the web interface. These are processed and stored in S3 for notification.

## Future Enhancements

- **Add SMS Notifications**: Use Amazon SNS to send SMS alerts in addition to email.
- **Improve UI**: Enhance the user interface for the disaster reporting website.
- **Add More Sensors**: Simulate more disaster types like wildfires, tsunamis, etc.
