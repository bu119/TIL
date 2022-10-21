from django.shortcuts import redirect, render
from django.views.decorators.http import require_safe, require_http_methods, require_POST
# require_safe이 get이다.
from todos.forms import TodoForm 
from .models import Todo 

# Create your views here.
@require_safe
def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    # todos = Todo.objects.all() # 내꺼만 보이려면 다 가져오면 안됌
    # todos = Todo.objects.order_by # 모두 만들어진 순서대로 정렬해서 가져오기
    # todos = Todo.objects.order_by('-pk')  # -pk 내림차순

    todos = request.user.todo_set.all() # 현재 접속한 유저를 참조하는 todos 모여
    
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():                     # 유효성 검사
            todo = form.save(commit=False)      # db에 저장하기 전에 
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:                                       # 처음 입력 받는 form 만들기
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)

def toggle(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')       # 로그인 안하면 보내버림

    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index')

@require_POST
def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login') 
    
    todo = Todo.objects.get(pk=pk)
    if request.user == todo.author:
        todo.delete()
    return redirect('todos:index')