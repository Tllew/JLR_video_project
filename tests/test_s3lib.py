import pytest
import boto3
from tempfile import NamedTemporaryFile
from ..src.s3lib import S3Lib
from moto import mock_s3
import json


@mock_s3
def test_getData():
    # conn = boto3.resource("s3", region_name="us-east-1")
    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket="test_bucket")
    expected = {
        "event": "zebraCrossing",
        "date": "10/02/2022",
        "startTime": "1034985675",
        "endTime": "1034985675",
        "videoUrl": "s3bucket video url",
        "examined": False,
    }

    conn.put_object(Bucket="test_bucket", Body=json.dumps(expected), Key="123.json")
    s3client = S3Lib()
    body = s3client.getData("123")

    assert body == expected


@mock_s3
def test_putData():
    conn = boto3.resource("s3", region_name="us-east-1")
    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket="test_bucket")
    expected = {
        "event": "zebraCrossing",
        "date": "10/02/2022",
        "startTime": "1034985675",
        "endTime": "1034985675",
        "videoUrl": "s3bucket video url",
        "examined": False,
    }
    s3client = S3Lib()
    s3client.putData("245", expected)

    conn = boto3.resource("s3", region_name="us-east-1")
    obj = conn.Object("test_bucket", "245.json")
    results = obj.get()["Body"].read().decode("utf-8")

    assert json.loads(results) == expected
