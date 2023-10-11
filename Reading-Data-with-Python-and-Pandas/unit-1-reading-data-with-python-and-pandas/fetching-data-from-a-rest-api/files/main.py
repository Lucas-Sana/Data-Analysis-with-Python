import pandas as pd
import requests
from pandas.io.json import json_normalize

api_url = "http://api.citybik.es/v2/networks"
req = requests.get(api_url)

if req.ok:
    json_dict = req.json()
    citybikes = pd.DataFrame.from_dict(json_dict['networks'])

    citybikes_unpacked = json_normalize(json_dict['networks'], sep='_')

    citybikes_unpacked.to_json('out.json')

    r = requests.get('https://httpbin.org/basic-auth/myuser/mypasswd', auth=('myuser', 'mypasswd'))

    if r.status_code == 200:
        authenticated_data = r.json()
        print(authenticated_data)
    else:
        print(f"Authentication failed with status code {r.status_code}")
else:
    print(f"Failed to fetch data. Status code: {req.status_code}")
