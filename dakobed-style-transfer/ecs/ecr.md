
aws --profile=admin iam create-user --user-name=usr1

$ aws --profile=admin iam attach-user-policy --user-name usr1 --policy-arn arn:aws:iam::<account number>:policy/authOnly


aws ecr create-repository --repository-name=dakobed-spring

aws --profile admin ecr set-repository-policy --repository-name dakobed-spring --policy-text file://usr1Policy.json

list images in rep
aws --profile usr1 ecr list-images --repository-name=dakobed-spring

$ aws --profile admin ecr set-repository-policy --repository-name dakobed-spring --policy-text file://usr1Policy.json

aws --profile usr1 ecr list-images --repository-name=dakobed-spring

aws ecs register-task-definition --cli-input-json file://./task.json