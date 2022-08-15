import requests as req
import pandas as pd

response = req.get("http://instagram.com")

print(response)

visitors = [1234, 5232, 9223, 8856, 7752]
errors = [23, 52, 62, 89, 12]

df = pd.DataFrame( {"visitors": visitors, "errors": errors}, index=["Mon", "Tue", "Wed", "Thu", "Fri"] )

print(df)

# DataFrame operator method [Mean, Average, Sum, etc]
errors_mean = df["errors"].mean()
print(errors_mean)