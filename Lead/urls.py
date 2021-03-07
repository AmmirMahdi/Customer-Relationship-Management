from django.urls import path, include
from Lead.views import LeadListView,LeadDetailView,LeadCreateView,LeadUpdateView,LeadDeleteView,register


from django.contrib.auth.views import LoginView


app_name = 'lead'
urlpatterns = [
    path('',LeadListView.as_view(), name='list'),
    path('list/<int:pk>',LeadDetailView.as_view(), name='detail'),
    path('create/',LeadCreateView.as_view(), name='create'),
    path('update/<int:pk>',LeadUpdateView.as_view(), name='update'),
    path("delete/<int:pk>",LeadDeleteView.as_view(), name='delete'),

    path('register/', register, name='register'),


    
]
