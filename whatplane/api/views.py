from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import PlaneSerializer, UserProfileSerializer
from .models import Plane, UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import requests

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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getPlanes(request):
    user_profile = request.user.userprofile
    planes = user_profile.planes.all()
    serializer = PlaneSerializer(planes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
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

   
    lat = data['lat']
    lon = data['lon']

    radius =50


        # Make the external API call
    response = requests.get(f"https://api.adsb.lol/v2/closest/{lat}/{lon}/{radius}")
    
    # Check if the request was successful
    if response.status_code == 200:
        adsb_data = response.json()  # Parse JSON response
    else:
        return Response({"error": "Failed to fetch data"}, status=response.status_code)

    if not adsb_data["ac"]:
        return Response({"detail": "No planes found"}, status=status.HTTP_200_OK)

    plane_info = adsb_data["ac"][0]
    type = plane_info.get("t")
    reg = plane_info.get("r")


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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletePlane(request):

    user_profile = request.user.userprofile
    data = request.data
    plane_id = data['id']
    plane_to_remove = get_object_or_404(Plane, id=plane_id)
    user_profile.planes.remove(plane_to_remove)
    return Response('Plane Removed')


@api_view(['GET'])
def getScores(request):
    top_users = UserProfile.objects.order_by('-score')[:10]  # Get top 10 users sorted by score
    serializer = UserProfileSerializer(top_users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)