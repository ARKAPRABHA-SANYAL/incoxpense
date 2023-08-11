from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.savings_table, name="savings"),
    #path('search-savings', csrf_exempt(views.search_savings),
     #    name="search_savings"),
    #path('savings_source_summary/', views.savings_source_summary,
     #    name="savings_source_summary"),
    #path('savingsstats/', views.savingsstats_view,
     #    name="savingsstats") 
]   