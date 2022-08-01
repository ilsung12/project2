from django.contrib import admin
from todo.models import Todo # model파일의 Todo.todo 를 가져옴

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    # admin 에서 보여줄 컬럼
    list_display = ('id', 'name', 'todo')