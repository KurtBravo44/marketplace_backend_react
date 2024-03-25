from rest_framework import pagination
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.serializers import *
from ads.models import Ad


class DefaultPagination(pagination.PageNumberPagination):
    page_size = 4


# __Ads Views__
# _______________

class AdListCreateAPIView(generics.ListCreateAPIView):
    """
    Класс возвращает все объявления при GET-запросе
    Класс создает объявление при POST-запросе
    """
    serializer_class = AdDefaultSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination


class MyAdListAPIView(generics.ListAPIView):
    """
    Класс возвращает все объявления текущего пользователя
    """
    serializer_class = AdDefaultSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class AnotherAdRetrieveAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    Класс возвращает объявление по его айди при GET-Запросе
    Класс редактирует объявление по его айди при PATCH-Запросе
    Класс удаляет объявление по его айди при DELETE-Запросе
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    queryset = Ad.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) and (self.request.user.role != 'admin'):
            raise ValidationError('Вы не Автор')

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) and (self.request.user.role != 'admin'):
            raise ValidationError('Вы не Автор')

        return super().destroy(request, *args, **kwargs)



# __Comments Views__
# ____________________

class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    Класс возвращает коментарии при GET-запросе
    Класс создает комментарий при POST-запросе
    """
    serializer_class = CommentDefaultSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs['ad_pk'])


class AnotherCommentRetrieveAPIView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    Класс возвращает комментарий по его айди при GET-Запросе
    Класс редактирует комментарий по его айди при PATCH-Запросе
    Класс удаляет комментарий по его айди при DELETE-Запросе
    """
    serializer_class = CommentDefaultSerializer
    queryset = Comment.objects.all()
    pagination_class = [IsAuthenticated]
    #lookup_field = 'ad_pk'

    def get_object(self):
        ad_pk = self.kwargs.get('ad_pk')
        comment_id = self.kwargs.get('id')
        return get_object_or_404(Comment, pk=comment_id, ad=ad_pk)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) and (self.request.user.role != 'admin'):
            raise ValidationError('Вы не Автор')

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if (self.request.user != obj.author) and (self.request.user.role != 'admin'):
            raise ValidationError('Вы не Автор')

        return super().destroy(request, *args, **kwargs)