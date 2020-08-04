

#
# import boto3
# client = boto3.client('ecs')
# cluster_response = client.create_cluster(
#     clusterName='my_cluster',
# )
#
#
# response = client.register_task_definition(
#     family='string',
#     taskRoleArn='string',
#     executionRoleArn='string',
#     networkMode='bridge'|'host'|'awsvpc'|'none',
#     containerDefinitions=[
#         {
#             'name': 'string',
#             'image': 'string',
#             'repositoryCredentials': {
#                 'credentialsParameter': 'string'
#             },
#             'cpu': 123,
#             'memory': 123,
#             'memoryReservation': 123,
#             'links': [
#                 'string',
#             ],
#             'portMappings': [
#                 {
#                     'containerPort': 123,
#                     'hostPort': 123,
#                     'protocol': 'tcp'|'udp'
#                 },
#             ],
#             'essential': True|False,
#             'entryPoint': [
#                 'string',
#             ],
#             'command': [
#                 'string',
#             ],
#             'environment': [
#                 {
#                     'name': 'string',
#                     'value': 'string'
#                 },
#             ],
#             'environmentFiles': [
#                 {
#                     'value': 'string',
#                     'type': 's3'
#                 },
#             ],
#             'mountPoints': [
#                 {
#                     'sourceVolume': 'string',
#                     'containerPath': 'string',
#                     'readOnly': True|False
#                 },
#             ],
#             'volumesFrom': [
#                 {
#                     'sourceContainer': 'string',
#                     'readOnly': True|False
#                 },
#             ],
#             'linuxParameters': {
#                 'capabilities': {
#                     'add': [
#                         'string',
#                     ],
#                     'drop': [
#                         'string',
#                     ]
#                 },
#                 'devices': [
#                     {
#                         'hostPath': 'string',
#                         'containerPath': 'string',
#                         'permissions': [
#                             'read'|'write'|'mknod',
#                         ]
#                     },
#                 ],
#                 'initProcessEnabled': True|False,
#                 'sharedMemorySize': 123,
#                 'tmpfs': [
#                     {
#                         'containerPath': 'string',
#                         'size': 123,
#                         'mountOptions': [
#                             'string',
#                         ]
#                     },
#                 ],
#                 'maxSwap': 123,
#                 'swappiness': 123
#             },
#             'secrets': [
#                 {
#                     'name': 'string',
#                     'valueFrom': 'string'
#                 },
#             ],
#             'dependsOn': [
#                 {
#                     'containerName': 'string',
#                     'condition': 'START'|'COMPLETE'|'SUCCESS'|'HEALTHY'
#                 },
#             ],
#             'startTimeout': 123,
#             'stopTimeout': 123,
#             'hostname': 'string',
#             'user': 'string',
#             'workingDirectory': 'string',
#             'disableNetworking': True|False,
#             'privileged': True|False,
#             'readonlyRootFilesystem': True|False,
#             'dnsServers': [
#                 'string',
#             ],
#             'dnsSearchDomains': [
#                 'string',
#             ],
#             'extraHosts': [
#                 {
#                     'hostname': 'string',
#                     'ipAddress': 'string'
#                 },
#             ],
#             'dockerSecurityOptions': [
#                 'string',
#             ],
#             'interactive': True|False,
#             'pseudoTerminal': True|False,
#             'dockerLabels': {
#                 'string': 'string'
#             },
#             'ulimits': [
#                 {
#                     'name': 'core'|'cpu'|'data'|'fsize'|'locks'|'memlock'|'msgqueue'|'nice'|'nofile'|'nproc'|'rss'|'rtprio'|'rttime'|'sigpending'|'stack',
#                     'softLimit': 123,
#                     'hardLimit': 123
#                 },
#             ],
#             'logConfiguration': {
#                 'logDriver': 'json-file'|'syslog'|'journald'|'gelf'|'fluentd'|'awslogs'|'splunk'|'awsfirelens',
#                 'options': {
#                     'string': 'string'
#                 },
#                 'secretOptions': [
#                     {
#                         'name': 'string',
#                         'valueFrom': 'string'
#                     },
#                 ]
#             },
#             'healthCheck': {
#                 'command': [
#                     'string',
#                 ],
#                 'interval': 123,
#                 'timeout': 123,
#                 'retries': 123,
#                 'startPeriod': 123
#             },
#             'systemControls': [
#                 {
#                     'namespace': 'string',
#                     'value': 'string'
#                 },
#             ],
#             'resourceRequirements': [
#                 {
#                     'value': 'string',
#                     'type': 'GPU'|'InferenceAccelerator'
#                 },
#             ],
#             'firelensConfiguration': {
#                 'type': 'fluentd'|'fluentbit',
#                 'options': {
#                     'string': 'string'
#                 }
#             }
#         },
#     ],
#     volumes=[
#         {
#             'name': 'string',
#             'host': {
#                 'sourcePath': 'string'
#             },
#             'dockerVolumeConfiguration': {
#                 'scope': 'task'|'shared',
#                 'autoprovision': True|False,
#                 'driver': 'string',
#                 'driverOpts': {
#                     'string': 'string'
#                 },
#                 'labels': {
#                     'string': 'string'
#                 }
#             },
#             'efsVolumeConfiguration': {
#                 'fileSystemId': 'string',
#                 'rootDirectory': 'string',
#                 'transitEncryption': 'ENABLED'|'DISABLED',
#                 'transitEncryptionPort': 123,
#                 'authorizationConfig': {
#                     'accessPointId': 'string',
#                     'iam': 'ENABLED'|'DISABLED'
#                 }
#             }
#         },
#     ],
#     placementConstraints=[
#         {
#             'type': 'memberOf',
#             'expression': 'string'
#         },
#     ],
#     requiresCompatibilities=[
#         'FARGATE',
#     ],
#     cpu='string',
#     memory='string',
#     tags=[
#         {
#             'key': 'string',
#             'value': 'string'
#         },
#     ],
#     pidMode='host'|'task',
#     ipcMode='host'|'task'|'none',
#     proxyConfiguration={
#         'type': 'APPMESH',
#         'containerName': 'string',
#         'properties': [
#             {
#                 'name': 'string',
#                 'value': 'string'
#             },
#         ]
#     },
#     inferenceAccelerators=[
#         {
#             'deviceName': 'string',
#             'deviceType': 'string'
#         },
#     ]
# )