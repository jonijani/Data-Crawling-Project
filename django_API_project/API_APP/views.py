from django.shortcuts import render

from wd_search.main import get_search_results_from_keyword
import json
from django.http import JsonResponse

def get_search_result(request,keyword):
    data = get_search_results_from_keyword(keyword)
    json_data = JsonResponse(data,safe=False)

    return json_data