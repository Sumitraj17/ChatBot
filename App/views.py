from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from App.models import Room, Message

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    try:
        room_details = Room.objects.get(name=room)
    except Room.DoesNotExist:
        room_details = Room.objects.create(name=room)
        
    props = {'username': username, 'room_details': room_details, 'room': room}
    return render(request, 'room.html', props)

def checkroom(request):
    room = request.POST['room_name']
    username = request.POST['username']
    password = request.POST['password']
    if Room.objects.filter(name=room).exists():
        room_details = Room.objects.get(name=room)
        if room_details.password == password:
            return JsonResponse({'success': True, 'redirect_url': '/' + room + '/?username=' + username})
        else:
            return JsonResponse({'success': False, 'error': 'Incorrect password'}, status=400)
    else:
        new_room = Room.objects.create(name=room, password=password)
        new_room.save()
        return JsonResponse({'success': True, 'redirect_url': '/' + room + '/?username=' + username})

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
