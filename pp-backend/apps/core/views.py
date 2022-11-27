from django.db import transaction
from django.shortcuts import get_object_or_404

from rest_framework.exceptions import APIException, ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers

from apps.core.models import Item

class ItemSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d")
    updated = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model  = Item
        fields = '__all__'

class ManageItem(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class   = ItemSerializer

    def post(self, request):
        try:
            user        = request.user
            name        = request.POST.get('name')
            description = request.POST.get('description')
            img         = request.FILES.get('img')
            
            with transaction.atomic():
                item             = Item()
                item.name        = name
                item.description = description
                item.img         = img
                item.save()

                serializer = self.serializer_class(item)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            data = {'error': str(e)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            item_id = request.POST.get('item_id')

            with transaction.atomic():
                item = get_object_or_404(Item, id=int(item_id))
                item.img.delete(save=True)
                item.delete()

                return Response(True, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {'error': str(e)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListItem(APIView):
    serializer_class   = ItemSerializer

    def get(self, request):
        try:
            items = Item.objects.all().order_by('-id')

            serializer = self.serializer_class(items, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            data = {'error': str(e)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VoteItem(APIView):
    serializer_class   = ItemSerializer

    def post(self, request):
        try:
            item_id = request.POST.get('item_id')

            with transaction.atomic():
                item = get_object_or_404(Item, id=int(item_id))
                item.votes += 1
                item.save()

                serializer = self.serializer_class(item)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {'error': str(e)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)