from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search_view, name='search'),
    path('results/<int:search_id>/', views.results_view, name='results'),
    path('refresh/<int:search_id>/', views.refresh_view, name='refresh'),
    path('history/', views.history_view, name='history'),

]
