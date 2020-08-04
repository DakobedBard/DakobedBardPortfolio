#!/bin/bash
aws s3 cp s3://dakobed/${style_dir} transfer --recursive
python3 transfer.py
#python3 uploadS3.py