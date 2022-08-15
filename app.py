import requests as req
 
response = req.get("http://instagram.com")

print(response.text)