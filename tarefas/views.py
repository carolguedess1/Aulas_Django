from django.shortcuts import render, get_object_or_404, redirect
from . models import Tarefa
from .forms import TarefaForm

# Create your views here.
def inicio(request):
    tarefas_list = Tarefa.objects.all().order_by('-create_at')
    return render(request, 'tarefas/index.html', {'var_tarefas': tarefas_list})

def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefa, pk= id)
    return render(request, 'tarefas/view_tarefa.html', {'tarefa': tarefa})

def novaTarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        form.save()
        return redirect('/')
    else:
        form = TarefaForm()
        return render(request, 'tarefas/addTarefa.html', {'form': form})