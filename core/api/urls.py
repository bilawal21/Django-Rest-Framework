from django.urls import path
from home.views import index, person, login, PersonAPI

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('login/', login),
    path('persons/',PersonAPI.as_view())
]