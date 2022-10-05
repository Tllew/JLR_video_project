import boto3


from moto import mock_s3

BUCKET_NAME = "test_bucket"
FILE_NAME = "red.jpg"
FILE_LOCATION = FILE_NAME


@mock_s3
def test_client():
    create_bucket()
    s3 = boto3.client("s3")

    with open(FILE_LOCATION, "rb") as data:
        s3.upload_fileobj(data, BUCKET_NAME, FILE_NAME)
    verify_upload()


@mock_s3
def test_resource():
    s3_resource, _ = create_bucket()
    s3_resource.meta.client.upload_file(FILE_LOCATION, BUCKET_NAME, FILE_NAME)
    #
    verify_upload()


@mock_s3
def test_bucket_resource():
    _, bucket = create_bucket()
    bucket.upload_file(FILE_LOCATION, FILE_NAME)
    #
    verify_upload()


def verify_upload():
    client = boto3.client("s3")
    resp = client.get_object(Bucket=BUCKET_NAME, Key=FILE_NAME)
    content_length = resp["ResponseMetadata"]["HTTPHeaders"]["content-length"]
    print("Content-Length: {}".format(content_length))


def create_bucket():
    s3 = boto3.resource("s3")
    bucket = s3.create_bucket(Bucket=BUCKET_NAME)
    return s3, bucket
