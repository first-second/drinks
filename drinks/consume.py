from getpass import getpass
import requests
url = 'http://127.0.0.1:8000/api-token-auth/'
username=input("enter username : ")
password=getpass("enter password : ")
data = {'username': username, 'password': password}
response = requests.post(url, data=data)
response_data=response.json()
token=response_data['token']
headers = {'Authorization': 'Token ' + token}
response=requests.get('http://127.0.0.1:8000/drinks/',headers=headers)
print(response.json())