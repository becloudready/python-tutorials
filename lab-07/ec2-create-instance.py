import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-054362537f5132ce2',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='ansible',
     SecurityGroups=[
        'ansible-node',
    ],
)