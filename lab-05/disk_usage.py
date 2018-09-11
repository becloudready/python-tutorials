import paramiko

wrong change

server_list=['localhost']
mount_point = '/dev/mapper/fedora-root'
threashold = 90

def check_disk(server,mount_point):
	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s.connect('localhost', username='chandank', password='password',
		allow_agent=False,look_for_keys=False)
	err,out,ins = s.exec_command("df -h")
	ss=out.read()
	for line in ss.split('\n'):
		#print(line.split()[0])
		if len(line.split()) > 0:
			if line.split()[0] == mount_point:
			#print(line.split()[0])
				return int(line.split()[4].rstrip('%'))

for server in server_list:
	print(server)
	disk_usage=check_disk(server,mount_point)
	if disk_usage > threashold:
		print('Sending email')
	else:
		print('All is well')

		
