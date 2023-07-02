from fastapi import FastAPI
import json
from wd_scrapper import get_search_results_from_keyword

app = FastAPI()

@app.get('/')
def home():
    return 'hello world'


@app.get('/junaid')
def get_junaid_data():
    data = {
            'name':'junaid',
            'age' : 33,
            'city':'london'
    }
    #json_data = json.dumps(data)
    return data


# API end point > '/wd-search/keyword'

@app.get('/wd-search/{keyword}')
def get_searched_data(keyword:str):
    try:
        data = get_search_results_from_keyword(keyword)
        #raise Exception('custom excpetion ')
        return data
    except Exception as e:
        error_dic = {
            'message':'something went wrong',
            'exception': str(e)
        }
        return error_dic










# @app.get('/shailesh')
# def get_shailesh_data():
#     data = {
#         'name' : None,
#         'age' : None,
#         'city' : None
#     }

#     return data
    


    

