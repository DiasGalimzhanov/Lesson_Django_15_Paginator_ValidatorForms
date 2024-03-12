from django.urls import path
from .views import PhoneList, PhoneCreate

urlpatterns = [
    path('', PhoneList.as_view(), name='home'),
    path('create/', PhoneCreate.as_view(), name='create')
]