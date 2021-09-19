from django.urls import path
from .views import createFakeData, showFakeData, homepage

urlpatterns=[
    path('', homepage, name='home'),

    path('createfake',createFakeData, name='createfake'),
    path('showfake', showFakeData, name='showfake')

]