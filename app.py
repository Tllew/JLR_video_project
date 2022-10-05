from flask import Flask

from .src.s3lib import S3Lib

app = Flask(__name__)


@app.route("/display/<int:dataId>")
def display(dataId):
    s3lib = S3Lib()
    return s3lib.getData(dataId)


@app.route("/examined/<int:dataId>")
def examined(dataId):
    s3lib = S3Lib()
    results = s3lib.getData(dataId)
    results["examined"] = True
    s3lib.putData(dataId, results)
