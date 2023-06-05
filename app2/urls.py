from django.urls import path
app_name='app2'
from app2.views import *
urlpatterns=[
    path('third/',third,name='third'),
    path('fourth/',fourth,name='fourth'),
]