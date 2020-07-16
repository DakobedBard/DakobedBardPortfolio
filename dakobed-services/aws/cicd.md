aws s3 mb s3://dakobed-cicid-artifacts

aws s3api put-bucket-policy --bucket dakobed-cicid-artifacts --policy file://artifacts-bucket-policy.json

#### Create code respository

aws codecommit create-repository --repository-name DakobedServiceRepository
aws codebuild create-project --cli-input-json file://code-build-project.json
arn:aws:iam::710339184759:role/DakobedServiceCodeBuildServiceRole

aws codebuild create-project --cli-input-json file://code-build-project.json