from importlib.resources import path
from django.urls import path
from . import views


app_name = 'todo_app'


urlpatterns = [
    path("", views.index, name="index"),
    
    path("<int:todo_id>/update", views.details_for_update, name="details_for_update"),
    path("<int:todo_id>/delete", views.details_for_delete, name="details_for_delete"),
    path("<int:todo_id>/read", views.details_for_read, name="details_for_read"),
    path("delete_all_todos", views.details_for_delete_all_todos, name="details_for_delete_all_todos"),



    path("update_todo/", views.update_todo, name="update_todo"),
    path("delete_todo/", views.delete_todo, name="delete_todo"),
    path("delete_todos/", views.delete_all_todos, name="delete_all_todos"),
    path("read_todo/", views.read_todo, name="read_todo"),
    path("search_todo/", views.search_todo, name="search_todo"),

    path("create_todo", views.create_todo, name="create_todo")
]
