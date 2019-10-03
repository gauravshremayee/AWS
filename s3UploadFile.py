
from flask import Flask, request 
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <input type=file name=pyFile>
    <input type=submit>
    </form>'''

@app.route('/upload', methods=['POST'])
def upload():
    s3 = boto3.resource('s3')

    s3.Bucket('prettyprinted').put_object(Key='pythonFile.py', Body=request.files['pyFile'])

    return '<h1>File saved to S3</h1>'

if __name__ == '__main__':
