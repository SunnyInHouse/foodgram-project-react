"""
Описание кастомных mixins.
"""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class CustomCreateDeleteMixin(DestroyModelMixin, CreateModelMixin,
                              GenericViewSet):

    serializer_class = None
    model_class = None
    error = 'Указанный объект не был добавлен в список'
    list_object = 'favorite'
    data_field_name = 'recipe'

    def create(self, request, id):

        serializer = self.serializer_class(
                data={
                    self.data_field_name: id,
                    'user': request.user.id,
                    'type_list': self.list_object,
                },
                context={
                    'request': request,
                }
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):

        user = request.user
        obj = get_object_or_404(self.model_class, id=id)

        if self.list_object == 'favorite':
            queryset = user.favorite_recipes
        if self.list_object == 'shopping':
            queryset = user.shopping_recipes
        if self.list_object == 'subscribing':
            queryset = user.subscribing

        if queryset.filter(id=id).exists():
            queryset.remove(obj)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {'errors': f'{self.error}', },
            status=status.HTTP_400_BAD_REQUEST
        )
