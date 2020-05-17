
import requests
import json
import configparser,os
from os.path import expanduser

config = configparser.ConfigParser()
config.read(os.path.join(expanduser("~"),".digitalocean/credentials"))
auth_token = config.get("default","auth_token")


url = "https://api.digitalocean.com/v2/droplets"

payload = {}
headers = {
  'Authorization': 'Bearer {}'.format(auth_token)
}

response = requests.request("GET", url, headers=headers, data = payload)

j = json.loads(response.text.encode('utf8'))
for dl in j['droplets']:
    print (dl['networks']['v4'][0]['ip_address'])

url = "https://api.digitalocean.com/v2/droplets?page=2&per_page=20"
response = requests.request("GET", url, headers=headers, data = payload)
j = json.loads(response.text.encode('utf8'))
for dl in j['droplets']:
    print (dl['networks']['v4'][0]['ip_address'])

url = "https://api.digitalocean.com/v2/droplets?page=3&per_page=20"
response = requests.request("GET", url, headers=headers, data = payload)
j = json.loads(response.text.encode('utf8'))
for dl in j['droplets']:
    print (dl['networks']['v4'][0]['ip_address'])