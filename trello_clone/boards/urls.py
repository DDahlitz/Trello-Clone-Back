from django.urls import path, include
from . import views

urlpatterns = [
    path('', BoardList.as_view(), name='board_list'),
    path('<int:pk>/', BoardDetail.as_view(), name='board_detail'),
    path('items/', ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('lists/', ListList.as_view(), name='list_list'),
    path('lists/<int:pk>/', ListDetail.as_view(), name='list_detail'),
]