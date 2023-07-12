from django.shortcuts import render
#from ..crawling_module.wd_scrapper import get_search_results_from_keyword
from crawling_module.wd_scrapper import get_search_results_from_keyword
import json
from django.http import JsonResponse


#    path('/<str:keyword>/', get_search_result, name='get_search_result')
def get_search_result(request,keyword):
    data = get_search_results_from_keyword(keyword)
    json_data = JsonResponse(data,safe=False)

    return json_data



# python data class
# pydantic schema
