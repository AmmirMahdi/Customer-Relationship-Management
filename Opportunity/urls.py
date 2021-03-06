from django.urls import path, include
from Opportunity.views import (OOPListView,OOPDetailView,OOPCreateView,OOPDeleteView,OOPUpdateView)



app_name = 'oop'
urlpatterns = [
    path('',OOPListView.as_view(), name='list'),
    path('list/<int:pk>',OOPDetailView.as_view(), name='detail'),
    path('create/',OOPCreateView.as_view(), name='create'),
    path('update/<int:pk>',OOPUpdateView.as_view(), name='update'),
    path("delete/<int:pk>",OOPDeleteView.as_view(), name='delete'),


    
]
