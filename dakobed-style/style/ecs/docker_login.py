import boto3
import docker
import base64

def log_into_aws_ecr(docker_client, region):
    # To do, set region
    ecr_client = boto3.client('ecr', region_name=region)

    # Get all repos
    response = ecr_client.describe_repositories()
    repo_names = []
    repositories = response.get('repositories', [])
    for repo in repositories:
        name = repo.get('repositoryName', '')
        if len(name):
            repo_names.append(name)
    token = ecr_client.get_authorization_token()
    username, password = base64.b64decode(token['authorizationData'][0]['authorizationToken']).decode('utf-8').split(":")
    registry_url = token['authorizationData'][0]['proxyEndpoint']
    login_results = docker_client.login(username, password, email='', registry=registry_url)

    prefix='https://'
    if registry_url.startswith(prefix):
        registry = registry_url[len(prefix):]
    else:
        registry = registry_url
    auth_config_payload = {'username': username, 'password': password }
    return ecr_client, repo_names, registry

docker_client = docker.from_env()

log_into_aws_ecr(docker_client,'us-west-2')