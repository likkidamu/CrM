import pandas as pd
import requests

api_key = "your_hubspot_api_key"
url = "https://api.hubapi.com/crm/v3/objects/contacts"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Load CSV
df = pd.read_csv("contacts.csv")

for _, row in df.iterrows():
    data = {
        "properties": {
            "email": row["email"],
            "firstname": row["firstname"],
            "lastname": row["lastname"],
            "phone": row["phone"]
        }
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())