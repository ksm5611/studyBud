from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
  {'id':1, 'name':'Lets learn python!'},
  {'id':2, 'name':'Design with me'},
  {'id':3, 'name':'Frontend developers'}
]

def home(req):
  context = {'rooms': rooms}
  return render(req, 'base/home.html', context)

def room(req, pk):
    room = None
    for i in rooms:
      if i['id'] == int(pk):
        room = i
    context = {'room': room}
    return render(req, 'base/room.html', context)