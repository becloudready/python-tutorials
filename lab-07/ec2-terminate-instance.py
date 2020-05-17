import boto3
import json

# Get all running instances
running_instances = []
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':
        print (instance.id , instance.state)
        ec2.instances.filter(InstanceIds = [instance.id]).terminate()

