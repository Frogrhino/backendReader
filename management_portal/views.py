from django.http import HttpResponse
from django.core import serializers
from management_portal.models import Manga
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from management_portal.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def mangaGetAll():
    return HttpResponse(serializers.serialize("json", Manga.objects.all()))


def mangaGetOne(request):
    return HttpResponse("test")


def mangaAdd(request):
    created = False
    try:
        Manga.objects.create(request)
        created = True

    except:
        created = False

    return HttpResponse(created)
