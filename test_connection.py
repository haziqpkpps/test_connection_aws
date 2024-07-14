import boto3
import psycopg2
from psycopg2 import sql
from flask import Flask, render_template_string

app = Flask(__name__)

# Replace these values with your RDS instance details
RDS_HOST = 'your-rds-endpoint.amazonaws.com'
RDS_PORT = 5432  # Default port for PostgreSQL
RDS_DB_NAME = 'yourdbname'
RDS_USER = 'yourusername'
RDS_PASSWORD = 'yourpassword'

# Replace this with your S3 bucket name
S3_BUCKET_NAME = 'your-s3-bucket-name'

def test_rds_connectivity():
    result = {"status": "", "message": ""}
    try:
        # Connect to the RDS instance
        connection = psycopg2.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            database=RDS_DB_NAME,
            user=RDS_USER,
            password=RDS_PASSWORD
        )
        cursor = connection.cursor()
        # Execute a simple query
        cursor.execute("SELECT 'Hello, World!'")
        result["message"] = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        result["status"] = "Success"
    except Exception as e:
        result["status"] = "Failed"
        result["message"] = str(e)
    return result

def test_s3_connectivity():
    result = {"status": "", "message": ""}
    try:
        s3 = boto3.client('s3')
        # List objects in the specified S3 bucket
        response = s3.list_objects_v2(Bucket=S3_BUCKET_NAME)
        if 'Contents' in response:
            objects = [obj['Key'] for obj in response['Contents']]
            result["message"] = objects
        else:
            result["message"] = "Bucket is empty or does not exist."
        result["status"] = "Success"
    except Exception as e:
        result["status"] = "Failed"
        result["message"] = str(e)
    return result

@app.route('/')
def index():
    rds_result = test_rds_connectivity()
    s3_result = test_s3_connectivity()
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS Connectivity Test</title>
    </head>
    <body>
        <h1>AWS Connectivity Test</h1>
        <h2>RDS Connectivity</h2>
        <p>Status: {{ rds_result.status }}</p>
        <p>Message: {{ rds_result.message }}</p>
        <h2>S3 Connectivity</h2>
        <p>Status: {{ s3_result.status }}</p>
        <p>Message: {{ s3_result.message }}</p>
    </body>
    </html>
    '''
    return render_template_string(html, rds_result=rds_result, s3_result=s3_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
