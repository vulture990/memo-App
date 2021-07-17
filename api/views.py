from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from api import serializers

# Create your views here.

@api_view(['GET'])
def getRoutes(resquest):
    routes=[
        {
            'Endpoint': '/todo/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of todos'
        },
         
         {
            'Endpoint': '/todo/id',
            'method':'GET',
            'body':None,
            'description':'Returns a todos object'
        },
         
        {
            'Endpoint': '/todo/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates a new todos with data sent in a post request'
        },
        {
            'Endpoint': '/todo/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description':'Create an existing todos with data sent in put req'
    
        },
        {
            'Endpoint': '/todo/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing todos'

        },
    
    ]
    return Response(routes)




@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)





@api_view(['GET'])
def getNote(request,pk):
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)



@api_view(['POST'])
def createNote(request):
    data=request.data
    note=Note.objects.create(
        body=data['body'],
    )
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(note,data=data)
    if serializer.is_valid():
        serializer.save()#SAVE OBJECT TO DB AFTER UPDATING
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('NOTE HAS BEEN DELETED')