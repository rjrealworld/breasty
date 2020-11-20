from . import  views
from django.urls import path
from django.contrib import admin


urlpatterns=[
    path("admin/", admin.site.urls),
    path("",views.index, name="index"),
    path("maps", views.base, name="base"),
    path("profile", views.profile, name="profile"),
    path("add_todo",views.add_todo, name="add_todo"),
    path("delete_todo/<int:todo_id>",views.delete_todo, name="delete_todo"),

]
