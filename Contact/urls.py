from django.urls import path 
from .views import ContactListView,ContactDetailView,ContactCreateView,ContactDeleteView, ContactUpdateView


app_name = 'contact'

urlpatterns = [
    path('', ContactListView.as_view(), name='list'),
    path('list/<int:pk>/',ContactDetailView.as_view(), name='detail'),
    path('create/',ContactCreateView.as_view(), name='create'),
    path('update/<int:pk>',ContactUpdateView.as_view(), name='update'),
    path("delete/<int:pk>",ContactDeleteView.as_view(), name='delete'),

]
