from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/',csrf_exempt(Registration.as_view())),
    path('',Checking.as_view())
]
