from flask import Flask

from bs4_test import get_search_results_from_keyword

app = Flask(__name__)  # __name__ accepts file name 

@app.route('/api/<string:keyword>',methods=['GET'])
def get_result(keyword):
    return get_search_results_from_keyword(keyword)




if __name__ == '__main__':
    app.run()




