# Tomos Williams Jaguar Landrover Video Project

**Architectural diagrams**

* Found in Overview

**Example code:**

A section of the envisioned flask microservice which shows a section of the code for updating whether or not a point of interest has been examined, this flag could be used to help test engineers manage their work and could provide stats using glue and athena to query the larger dataset


**Introduction**

*Run Code*
`pip install poetry`
`poetry build`
`export s3_bucket=test_bucket`
`poetry run flask run`

*Run Tests*
`export s3_bucket=test_bucket`
`pytest`
