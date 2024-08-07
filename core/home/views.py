from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer, LoginSerializer

from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['flask', 'django', 'tornado', 'fastApi'],
        'course_provider': 'Scaler'
    }
    if request.method == 'GET':
        print(request.GET.get('search'))
        print('You hit the GET method')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print(data['age'])
        print('You hit the POST method')
        return Response(courses)
    elif request.method == 'PUT':
        print('You hit the PUT method')
        return Response(courses)
    
@api_view(['POST']) 
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({'message': 'success'})

    return Response(serializer.errors)

class PersonAPI(APIView):
    def get(self, request):
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)
        # return Response({'message': 'This is get request'})
    
    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
        # return Response({'message': 'This is post request'})
    
    def put(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
        # return Response({'message': 'This is put request'})
    
    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
        # return Response({'message': 'This is patch request'})
    
    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})
        # return Response({'message': 'This is delete request'})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])    
def person(request):
    if request.method == 'GET':
        objs = Person.objects.filter(color__isnull = False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors) 
    
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors) 

    elif request.method == 'PATCH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data = data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors) 

    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'person deleted'})