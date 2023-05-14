from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Room, Message
from django.contrib.auth.models import User

@login_required
def rooms(request):
    users = User.objects.count()
    rooms = Room.objects.all()
    return render(request,'room/rooms.html',{'rooms': rooms, 'list_users':users})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html',{'room': room, 'messages': messages})
