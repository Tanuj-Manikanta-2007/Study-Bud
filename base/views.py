from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from .import models
from django.http import HttpResponse
from .forms import RoomForm, MessageForm, TopicForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
rooms = models.Room.objects.all()
# Create your views here.
def home(request):
  q = request.GET.get('q', '') 
  rooms = models.Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
    )
  room_count = rooms.count()
  room_messages = models.Message.objects.filter(Q(room__topic__name__icontains =q))[:5]
  topics = models.Topic.objects.all()
  return render(request,"base/home.html",{'name': 'Tanuj',"rooms" : rooms,"topics" : topics,'room_count':room_count,'room_messages' : room_messages})

def room(request,pk):
  room = rooms.get(id = int(pk))
  room_messages = room.message_set.all().order_by('-created')
  participants = room.participants.all()
  if request.method == 'POST':
    message = models.Message.objects.create(
      user = request.user,
      room = room,
      body = request.POST.get('body')
    )
    room.participants.add(request.user)
    return redirect('Room Page',pk = room.id)
  context = {'room' : room,'room_messages' : room_messages,'participants' : participants}
  return render(request,"base/room.html",context)
@login_required(login_url='Login')
def createRoom(request):
  form = RoomForm()

  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      room = form.save(commit = False)
      room.host = request.user
      room.save()
      return redirect('home')
     
  context = {'form' : form}
  return render(request,'base/room_form.html',context)

@login_required(login_url='Login')
def createTopic(request):
  form = TopicForm()

  if request.method == 'POST':
    form = TopicForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
     
  context = {'form' : form}
  return render(request,'base/topic_form.html',context)

@login_required(login_url= 'Login')
def updateRoom(request,pk):
  room = models.Room.objects.get(id = int(pk))
  if request.user != room.host:
    return HttpResponse('Your are not allowed here!!')
  form = RoomForm(instance = room)
  if request.method == 'POST':
    form = RoomForm(request.POST,instance = room)
    if form.is_valid():
      form.save()
      return redirect('home')
    
  context = {'form' : form}
  return render(request,'base/room_form.html',context)

@login_required(login_url= 'Login')
def deleteRoom(request,pk):
  room = get_object_or_404(models.Room,id = int(pk))
  if request.method == 'POST':
    room.delete()
    return redirect('home')
  return render(request,'base/delete.html',{'obj' : room})

def LoginPage(request):
  page = 'Login'
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == 'POST' :
   username = request.POST.get('username') 
   password = request.POST.get('password')
   user = authenticate(request,username = username,password = password)
   if user is not None:
     login(request,user)
     return redirect('home')
   else:
     messages.error(request,'Username or password does not exist')

  context = {'page' : page}
  return render(request,"login_register.html",context)

def logout_view(request):
  logout(request)
  return redirect('home')

def register(request):
  page = 'Register'
  form = UserCreationForm()
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if(form.is_valid()):
      user = form.save(commit = False)
      user.username = user.username.lower()
      user.save()
      login(request,user)
      return redirect('home')
    else:
      messages.error(request, 'An error occured during resgistration')

  return render(request,"login_register.html",{'form' : form})

@login_required(login_url= 'Login')
def deleteMessage(request,pk):
  message = get_object_or_404(models.Message,id = int(pk))
  if request.user != message.user:
    return HttpResponse('Your are not allowed here !!')
  if request.method == 'POST':
    message.delete()
    return redirect('home')
  return render(request,'base/delete.html',{'obj' : message})

@login_required(login_url= 'Login')
def updateMessage(request,pk):
  message = get_object_or_404(models.Message,id = int(pk))
  if request.user != message.user:
    return HttpResponse('Your are not allowed here !!')
  form = MessageForm(instance = message)
  if request.method == 'POST':
    form = MessageForm(request.POST,instance = message)
    if form.is_valid():
      form.save()
      return redirect('Room Page', pk=message.room.id)
    
  context = {'form' : form}
  return render(request,'base/message_form.html',context)

def userProfile(request,pk):
 
  user = get_object_or_404(User, id=pk)
  rooms = user.room_set.all()
  room_messages = user.message_set.all()
  topics = models.Topic.objects.all()
  context = {'user' : user,'rooms' : rooms, 'room_messages' : room_messages,'topics' : topics}
  return render(request,'base/profile.html',context)