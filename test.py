import requests
import json
import pandas as pd

# Step 1: Perform login request to obtain token
login_url = "https://registre-national-entreprises.inpi.fr/api/sso/login"

with open("login.json") as file:
    data = json.load(file)

response = requests.post(login_url, json=data)

if response.status_code != 200:
    print("Error during login. Status code:", response.status_code)
    exit()

token=response.json()["token"]

headers = {"Authorization": "Bearer "+token}
i=int(input(f'''what to search: \n
            companyName : 0
            Derigeant : 1
        '''))
search_text = input("Enter search text: ")
liste=["companyName","Derigeant"]

companies_url = "https://registre-national-entreprises.inpi.fr/api/companies"


params = {liste[i]: search_text}

response = requests.get(companies_url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    df= pd.DataFrame(data)
    print(df)
else: 
    print("Error during GET request. Status code:", response.status_code)



