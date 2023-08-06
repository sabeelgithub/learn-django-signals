from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import json


# Create your views here.


# User1 = get_user_model()
# user1 = User1(username='boss',email='anshi@gmail.com')
# user1.save()
# print(user1.get_username())
# print(user1.delete())

class Registration(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            print(data)
            if User.objects.filter(username=data['email']):
                print('This email is already taken')
                return HttpResponse('This email is already taken')
            elif User.objects.filter(username=data['username']):
                print('This username is already taken')
                return HttpResponse('This username is already taken')
            else:
                user = User.objects.create_user(email=data['email'],username=data['username'])
                user.save()
                return HttpResponse(f'user {user} is created succesfully')
            
        except Exception as e:
            print(e)
            return HttpResponse(e)
        

class Deleting(View):
    def delete(self,request,id):
        try:
            user = User.objects.get(id=id)
            if user:
                user.delete()
                return HttpResponse(f'user {user} deleted sussessfully')
        except Exception as e:
            print(e)
            return HttpResponse(f'user with id {id} not found')




