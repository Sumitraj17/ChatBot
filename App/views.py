from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from App.models import Room,Message
# Create your views here.
def home(request):
    print('home')
    return render(request,'home.html')

def room(request, room):
    username = request.GET.get('username')
    print(username)
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        room_details = Room.objects.create(name=room)
        
    props = {'username': username, 'room_details': room_details, 'room': room}
    return render(request, 'room.html', props)

def checkroom(request):
    # print('check')
    room = request.POST['room_name']
    username = request.POST['username']
    print(username)
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    print(username)
    new_message = Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request,room):
    # print('get message_sumit')
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    # print(messages.values())
    return JsonResponse({"messages":list(messages.values())})