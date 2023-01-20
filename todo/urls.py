from django.urls import path
from .views import *
urlpatterns = [
    path('/',index),
    path('index/',index,name="index"),
    path('insert/',insert),
    path('delete/<int:id>',delete,name='delete'),
    #path('edit/<int:id>',edit,name="edit"),
    path('update/<int:id>',update,name='update'),
    path('login/',login_user,name='login_user'),
    path('register/',register_user),
      path('logout/',logout_user),
]
