#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pulls data from the Rails and Go databases into the DS AWS S3 bucket.

Dependencies:
psycopg2==2.8.5
pandas==1.0.3
pyarrow==0.17.0
s3fs==0.4.2
boto3==1.12.49

Possible Databases: ['Go', 'Rails']
"""
import pd from pandas
