import paramiko
import os
from os.path import expanduser



server_list=['ec2-15-223-48-154.ca-central-1.compute.amazonaws.com']
mount_point = '/dev/xvda1'
threashold = 5

def check_disk(server,mount_point):
	k = paramiko.RSAKey.from_private_key_file(os.path.join(expanduser("~"),"ansible.pem"))
	c = paramiko.SSHClient()
	c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s.connect(server, username='ec2-user', pkey=k)
	err,out,ins = s.exec_command("df -h")
	ss=out.read()
	for line in ss.decode().split('\n'):
    		#print(line.split()[0])
		if len(line.split()) > 0:
			if line.split()[0] == mount_point:
			#print(line.split()[0])
				return int(line.split()[4].rstrip('%'))

for server in server_list:
	print("Connecting to Server : {}".format(server))
	disk_usage=check_disk(server,mount_point)
	if disk_usage > threashold:
		print('Disk {} is Full'.format(mount_point))
	else:
		print('All is well')

		
