from django.urls import path
from . import views
from django.http import StreamingHttpResponse
urlpatterns=[
    path('',views.home, name="home"),
    path('issue/',views.issue, name='issue'),
    
]