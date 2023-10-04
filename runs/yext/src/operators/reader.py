import json
import requests
import os
import yaml
from google.cloud import bigquery
import time

#limit mise à 5 au lieu de 50 pour ne pas surcharger les appels
limit = 50

def read(file):
    try:
        f = open("/app/src/" + file)
        return json.load(f)
    except Exception as inst:
        return {}

def get_config():
    if os.environ.get("ENV") == "prod":
        file = "config-prod.yaml"
    else:
        file = "config-staging.yaml"
    with open('/app/src/' + file) as f:
        return dict(yaml.load(f, Loader=yaml.FullLoader))


def structure(item):
    return json.dumps(item)
#clé de l'api à mettre comme variable d'env dans le docker run ( api secret manager)
#exemple déjà fait dans flows-magento
def yext_query(offset, limit):
    url = "https://api.yext.com/v2/accounts/me/entities?limit={limit}&offset={offset}&api_key={bearer}&v=20210101".format(
            offset=offset,
            limit=limit,
            bearer=os.environ.get("YEXT_BEARER")
        )

    answer = json.loads(requests.get(url).text)
    return list(map(structure, answer["response"]["entities"])), answer["response"]["count"]


def query_api():

    offset = 0
    data = yext_query(offset, limit)

    stores = data[0]
    total = data[1]
    offset += limit

    while offset <= total:
        stores += yext_query(offset, limit)[0]
        offset += limit
        time.sleep(1)
    return stores 

