from django.urls import path
from .views import get_search_result

app_name = 'wd_search'

urlpatterns = [
   path('<str:keyword>/', get_search_result, name='get_search_result')
    
]