from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import PlaneSerializer
from .models import Plane, UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def capturePlane(request):

    user_profile = request.user.userprofile
    
    data = request.data
    type = data['type']
    reg = data['reg']

    if user_profile.planes.count() >=5:
        return Response({"detail": "You can only own 5 planes."}, status=status.HTTP_400_BAD_REQUEST)

    plane, created = Plane.objects.get_or_create(
        reg = reg,
        type = type
    )

    if created or plane not in user_profile.planes.all():
        user_profile.planes.add(plane)
        message = f"Captured the plane: {type} with registration {reg}"
        #status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
    else:
        message = "Plane already captured."
        #status_code = status.HTTP_200_OK


    serializer = PlaneSerializer(plane, many=False)
    return Response({"message": message, "plane": serializer.data})

@api_view(['DELETE'])
def deletePlane(request, pk):

    plane = Plane.objects.get(id=pk)
    plane.delete()
    return Response('Plane Removed')