import argparse
import json
import requests

payload = {
	"mission_id": "8d2ad9ea-ce81-11ef-904a-000e8e9884eb",
	"message": "hello world", 
	"parameters": [
		{"id": "mach-target", "value": "3d7c7c40-ce85-11ef-904a-000e8e9884eb"}
	],
	"priority": 0
}
print(json.dumps(payload,indent=4))

headers = {
	"accept": "application/json",  
	"Authorization": "Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA==",
	"Accept-Language": "en_US",
	"Content-Type": "application/json"
}

url = 'http://mir.com/api/v2.0.0/missions'
response = requests.get(url,headers=headers)
missions = json.loads(response.text)
for mission in missions:
	if mission['name'] == "pr-mxi":
		mission_guid = mission['guid']

url = 'http://mir.com/api/v2.0.0/positions'
response = requests.get(url,headers=headers)
positions = json.loads(response.text)
for position in positions:
	if position['name'] == 'pr-mach-a':
		position_guid = position['guid']

url = "http://mir.com/api/v2.0.0/mission_queue"
payload = {
	"mission_id": mission_guid,
	"message": "hello world", 
	"parameters": [
		{"id": "mach-target", "value": position_guid}
	],
	"priority": 0
}
print(json.dumps(payload,indent=4))
response = requests.post(url, headers=headers, json=payload)
print(response)

url = "http://mir.com/api/v2.0.0/status"
payload = {"state_id": 3}
response = requests.put(url,headers=headers,json=payload)
print(response)

# if __name__ == "__main__":
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument("--host", help="Host", default=DEFAULT_HOST)
# 	parser.add_argument("--interval", help="Interval", default=DEFAULT_INTERVAL)