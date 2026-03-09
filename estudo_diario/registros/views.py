from django.shortcuts import render, redirect
from .models import RegistroEstudo
from django.shortcuts import get_object_or_404
from .forms import RegistroEstudoForm 

def home(request):
    registros = RegistroEstudo.objects.all().order_by('-data') 
    return render(request, 'registros/home.html', {'registros': registros})

def cadastro(request):
    # Verifica se o metodo de requisição e POST
    if request.method == 'POST':
        form = RegistroEstudoForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistroEstudoForm()
    
    return render(request, 'registros/cadastro.html', {'form': form})

def excluir(request, id):
    registro = get_object_or_404(RegistroEstudo, id=id)
    registro.delete()
    return redirect('home')