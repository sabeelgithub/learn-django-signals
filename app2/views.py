from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from .signals import custom_signal

# Create your views here.
def MyDetails(request,id):
    try:
        if request.method == 'GET':
            user = User.objects.get(id=id)
            if user:
                custom_signal.send(sender=None,arg1=user.username, arg2=user.email)
                return JsonResponse({'email':user.email,'username':user.username})
            return HttpResponse(f'user with id {id} does not exists')
        return HttpResponse('requested method not allowed')     
    except Exception as e:
        print(e)
        return HttpResponse(e)