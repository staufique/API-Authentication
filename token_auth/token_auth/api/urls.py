
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import StudentDetail
# from api.auth import CustomeAuthToken
urlpatterns = [
    path('studentapi/',StudentDetail.as_view()),
    path('studentapi/<int:pk>',StudentDetail.as_view()),
    # path('gettoken/',CustomeAuthToken.as_view()),
]