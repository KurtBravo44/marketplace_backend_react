from django.urls import include, path
from users.apps import UsersConfig


from users.views import *

app_name = UsersConfig.name


urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user_list_create'),
    path('me/', UserRetrieveUpdateAPIView.as_view(), name='user_retvieve_update'),
    path('set_password/', UserSetPasswordAPIView.as_view(), name='user_set_password'),
    path('<int:pk>/', AnotherUserRetrieveAPIView.as_view(), name='another_user_retrieve'),

]
