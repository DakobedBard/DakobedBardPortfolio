#!/bin/bash
aws ec2 run-instances --image-id ami-0a2363a9cff180a64 --security-group-ids sg-085dd4f3c078cb1ec \
 --user-data file://userdata.sh --instance-type g2.2xlarge --key-name corwin  --iam-instance-profile Name=S3fullaccess
