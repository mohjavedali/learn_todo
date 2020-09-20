from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-id")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = TodoForm
        page = {
            "form": form,
            "list": item_list,
            "title": "TODO LIST",
        }
    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item has been removed !!!")
    return redirect('/')