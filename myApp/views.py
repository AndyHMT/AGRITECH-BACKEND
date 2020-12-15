from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import ApiUser
from .serializers import ApiUserSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        apiUser = ApiUser.objects.all()
        serializer = ApiUserSerializer(apiUser, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ApiUserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, username):
    try:
        apiUser = ApiUser.objects.get(username=username)

    except ApiUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ApiUserSerializer(apiUser)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ApiUserSerializer(apiUser, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        apiUser.delete()
        return HttpResponse(status=204)
