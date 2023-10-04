import os
from src.extensions.bigquery import write as write_bq

def write(orders):
    if os.environ.get("ENV") == "prod":
        write_bq(orders)
    else:
        write_bq(orders)
