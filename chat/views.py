from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here.
from chat.models import Room,Message

def home(request):
    return render(request,'home.html')

def room(request,room_id):
    username=request.GET.get("username")
    print("username=",username)
    room_details_obj=Room.objects.get(id=room_id)
    context={'username':username,'room_name':room_details_obj.name,'room_details':room_details_obj}
    print("context=",context)
    return render(request,'room.html',context)
    
def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat/room/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/room/'+str(new_room.id)+'/?username='+username)


def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    new_message=Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessage(request,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    # print("messages=",messages)
    return JsonResponse({"message":list(messages.values())})