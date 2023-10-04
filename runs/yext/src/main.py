from src.operators.reader import read, query_api
from src.operators.formatter import format
from src.operators.reader import get_config
from src.operators.writer import write 
from functional import seq
import traceback
import json


def run():

    config= read("static/config.json")
    orders = list()
    chain = seq(0)\
            .flat_map(lambda x: query_api())\
            .map(lambda x: format(json.loads(x),config))\

    orders = orders + chain.list() 
    write(orders)
    return {"result": True}
            
if __name__ == '__main__':
    run()
