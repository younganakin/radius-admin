from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Radcheck, Nas
from .serializers import NasSerializer, RadcheckSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def radcheck_list(request):
    """
    List all radius users.
    """
    radchecks = Radcheck.objects.all()
    serializer = RadcheckSerializer(radchecks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def radcheck_create(request):
    """
    Create a new radius user.
    """
    serializer = RadcheckSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def radcheck_detail(request, macAddress, ssid):
    """
    Retrieve, update or delete a radius user.
    """
    try:
        radcheck = Radcheck.objects.get(macAddress=macAddress, ssid=ssid)
    except Radcheck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RacheckSerializer(radcheck)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RadcheckSerializer(radcheck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        radcheck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def nas_list(request):
    """
    List all radius nas.
    """
    nases = Nas.objects.all()
    serializer = NasSerializer(nases, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def nas_create(request):
    """
    Create a new radius nas.
    """
    serializer = NasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def nas_detail(request, nasname):
    """
    Retrieve, update or delete a radius user.
    """
    try:
        nas = Nas.objects.get(nasname=nasname)
    except Nas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NasSerializer(nas)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NasSerializer(nas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        nas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
