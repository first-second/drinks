from getpass import getpass
import requests
import pandas as pd
url = 'http://127.0.0.1:8000/api-token-auth/'
username=input("enter username : ")
password=getpass("enter password : ")
data = {'username': username, 'password': password}
response = requests.post(url, data=data)
response_data=response.json()
print(response_data)
print("+++++++++++++++++++++++++++++++++++")
token=response_data['token']
headers = {'Authorization': 'Token ' + token}
response=requests.get('http://127.0.0.1:8000/drinks/',headers=headers)
#response_test = requests.get('http://127.0.0.1:8000/drinks/')
#print(response_test.json())
print(response.json())
data = response.json()
print("+++++++++++++++++++++++++++++++++++")
df = pd.DataFrame(data)
print(df.to_string(index=False))