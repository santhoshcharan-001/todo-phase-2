from django.urls import path
from .views import home,get_tasks,delete,add_task,validate_login,login_arti,logout_arti
from .views import register,check_username
urlpatterns =[
    # path('',spandana),
    path('get_tasks/',get_tasks),
    path('delete_task/',delete),
    path('add_task/',add_task),
    path('',login_arti),
    path('home/',home),
    path('logout/',logout_arti,name="logout"),
    # path('login/','login_view'),
    path('validate_login/',validate_login,name='validate_login'),
    path('register/',register,name='register'),
    path('check_username/',check_username),
]