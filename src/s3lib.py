from unicodedata import category
import boto3
import os
import json


class S3Lib:
    def getData(self, dataId):
        s3 = boto3.resource("s3", region_name="us-east-1")
        obj = s3.Object(os.environ["s3_bucket"], f"{dataId}.json")
        results = obj.get()["Body"].read().decode("utf-8")
        return json.loads(results)

    def putData(self, dataId, data):
        s3 = boto3.client("s3", region_name="us-east-1")
        s3.put_object(
            Bucket=os.environ["s3_bucket"], Body=json.dumps(data), Key=f"{dataId}.json"
        )
