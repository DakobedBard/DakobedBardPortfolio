
### Create a repository for the streaming service

aws codecommit create-repository --repository-name DakobedStreamingServiceRepository


https://git-codecommit.us-west-2.amazonaws.com/v1/repos/DakobedStreamingServiceRepository



sam package --template-file ./real-time-streaming.yml --output-template-file ./transformed-streaming.yml --s3-bucket dakobed-lambda-sam