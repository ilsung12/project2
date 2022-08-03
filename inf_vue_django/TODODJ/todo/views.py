from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from todo.models import Todo
from django.urls import reverse_lazy # 생성전에 불러오는것을 방지

class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'


class TodoCV(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list') # 성공시 이동할 url (redirection)


class TodoLV(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'


class TodoDelV(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')

class TodoMOMCV(MultipleObjectMixin, CreateView):
    # 파이썬에서는 상속받는 순서가 중요하다. : (mixin, main)-> createView가 main
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form_list.html'
    success_url = reverse_lazy('todo:mixin')

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        # 상위클래스의 get 메소드를 호출 -> createView의 getContextData 메소드가 호출되어 object_list가 템플릿으로 넘어감
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

class TodoDelV2(DeleteView):
    model = Todo
    # template_name = 'todo/todo_confirm_delete.html' # 확인창 생략
    success_url = reverse_lazy('todo:mixin')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)