import requests as req
import pandas as pd

response = req.get("http://instagram.com")

print(response.text)

