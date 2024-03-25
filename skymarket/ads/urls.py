from django.urls import include, path
from ads.apps import SalesConfig
from ads.views import *


app_name = SalesConfig.name

urlpatterns = [
    path('', AdListCreateAPIView.as_view(), name='ad_list_create'),
    path('me/', MyAdListAPIView.as_view(), name='ad_my_list'),
    path('<int:id>/', AnotherAdRetrieveAPIView.as_view(), name='another_ad'),

    path('<int:ad_pk>/comments/', CommentListCreateAPIView.as_view(), name='comment_list'),
    path('<int:ad_pk>/comments/<int:id>/', AnotherCommentRetrieveAPIView.as_view(), name='another_com'),

]
