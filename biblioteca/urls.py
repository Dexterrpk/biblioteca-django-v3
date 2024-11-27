from django.urls import path
from .views import ColecaoListCreate, ColecaoDetail

urlpatterns = [
    path('colecoes/', ColecaoListCreate.as_view(), name='colecao-list-create'),
    path('colecoes/<int:pk>/', ColecaoDetail.as_view(), name='colecao-detail'),
]
