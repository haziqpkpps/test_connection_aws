# AWS Connectivity Test

This project tests the connectivity between an EC2 instance, an RDS instance, and an S3 bucket. The results are displayed on a webpage using Flask.

## Prerequisites

- Python 3.x
- AWS credentials with appropriate permissions
- An RDS instance (PostgreSQL)
- An S3 bucket

## Installation

1. **Install required libraries**:
   ```sh
   pip install boto3 psycopg2 flask
