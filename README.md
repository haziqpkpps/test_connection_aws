# AWS Connectivity Test

## Description
This repository contains a Python script that tests the connectivity between an EC2 instance, an RDS instance, and an S3 bucket. The results are displayed on a webpage using the Flask web framework. This project can be useful for ensuring that your AWS infrastructure components can communicate with each other properly.

## Features
- **RDS Connectivity Test**: Connects to a PostgreSQL RDS instance and executes a simple query.
- **S3 Connectivity Test**: Lists the objects in a specified S3 bucket.
- **Web Interface**: Displays the results of the connectivity tests on a webpage for easy viewing.

## Prerequisites
- Python 3.x
- AWS credentials with appropriate permissions
- An RDS instance (PostgreSQL)
- An S3 bucket

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/aws-connectivity-test.git
   cd aws-connectivity-test

## Run the apps
1. Install the requirements 
```sudo apt-get install libpq-dev - Ubuntu
   sudo yum install postgresql-devel - Centos
   pip install boto3 psycopg2-binary flask

2. Run the application :
```python3 test_connection.py