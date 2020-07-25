import boto3
import time

bootstrap_script = '''
#!/bin/bash
git clone https://github.com/MathiasDarr/Dakobed.git
cd Dakobed/mir



'''



def launch_instance(self, instance_type, PemKey, bootstrap_script=""):
    '''
    :param instance_type:
    :param PemKey:
    :param bootstrap_script:
    :return: instance ID
    Should this return the AWS instance ID or the models PK?? Probably the primary key..
    '''
    ec2 = boto3.resource('ec2', region_name='us-west-2')
    ami = 'ami-01a4e5be5f289dd12'
    instance = ec2.create_instances(
        ImageId=ami,
        MinCount=1,
        MaxCount=1,
        KeyName=PemKey,
        InstanceInitiatedShutdownBehavior='terminate',
        IamInstanceProfile={'Name': 'S3fullaccess'},
        InstanceType=instance_type,
        SecurityGroupIds=['sg-03915a624fb5bf7bd'],
        UserData=bootstrap_script
    )
    time.sleep(10)
    dns = self.get_name(instance[0].id)
    while dns == "":
        time.sleep(5)
        dns = self.get_name(instance[0].id)
    return instance


