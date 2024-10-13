from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlaneSerializer
from .models import Plane

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/planes',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of planes'
        },
        {
            'Endpoint': '/planes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single plane'
        },
        {
            'Endpoint': '/planes/capture',
            'method': 'POST',
            'body': None,
            'description': 'Adds a plane to the hangar'
        },
        {
            'Endpoint': '/planes/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Removes a plane from the hangar'
        },
        ]
    return Response(routes)

@api_view(['GET'])
def getPlanes(request):
    planes = Plane.objects.all()
    serializer = PlaneSerializer(planes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPlane(request, pk):
    plane = Plane.objects.get(id=pk)
    serializer = PlaneSerializer(plane, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPlane(request):
    data = request.data
    plane = Plane.objects.create(
        type = data['type'],
        reg = data['reg']
    )
    serializer = PlaneSerializer(plane, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePlane(request, pk):

    plane = Plane.objects.get(id=pk)
    plane.delete()
    return Response('Plane Removed')