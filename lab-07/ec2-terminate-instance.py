import boto3
import json

# Get all running instances
running_instances = []
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':
        print (instance.id , instance.state)

ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# print(response)

# for instance in response['Instances']:
#     print(instance)

response = ec2.terminate_instances(
    InstanceIds=[
        instance.id,
    ],
    DryRun=False
)
print(response)