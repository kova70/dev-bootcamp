#!/usr/bin/env bash
scp -i ~/.ssh/bootcamp example.py centos@ec2-35-162-238-120.us-west-2.compute.amazonaws.com:
ssh -i ~/.ssh/bootcamp centos@ec2-35-162-238-120.us-west-2.compute.amazonaws.com "export PYSPARK_PYTHON=/usr/bin/python3.6;spark-submit --master local example.py"
