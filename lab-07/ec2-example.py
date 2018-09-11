import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

# Mac installation tip: 
# sudo pip install --ignore-installed six boto3
# Assignment : Create 3 instances in ec2 using ansible playbooked from last week.
# One the instance are created.
# Use Python boto3 library to Parse the ouput of boto reponse and find 
# 1. instance ids, ip address, privateDns, Public DNS