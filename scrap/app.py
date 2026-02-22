import requests
res = requests.get("https://youtube.com")
print(f"status:{res.status_code}")
print(f"header:{res.headers}")
print(f"content:{res.content}")
