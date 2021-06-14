from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.data_list),
    path('set_list/', views.set_list),
    path('users/create', views.CreateUserView.as_view()),
    path('current_user/', views.get_current_user),
]