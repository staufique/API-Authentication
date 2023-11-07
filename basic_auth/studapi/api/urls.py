from django.urls import path
from api import views

urlpatterns = [
    path('studentapi/',views.StudentDetail().as_view()),
    path('studentapi/<int:pk>',views.StudentDetail1().as_view()),
    # path('studentapi/<int:id>',views.drink_detail),
]