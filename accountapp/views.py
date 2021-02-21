# Create your views here.

from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet, mixins

from accountapp.models import Account
from accountapp.serializers import *


class AccountViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrievßeModelMixin,
                     GenericViewSet):
    lookup_field = "id"
    permission_classes = [permissions.AllowAny, ]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

