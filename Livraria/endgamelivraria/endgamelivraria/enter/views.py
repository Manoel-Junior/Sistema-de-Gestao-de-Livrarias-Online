from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import redirect


def Index_livros(request):
        livro = Livro.objects.all()
        return render(request, 'enter/index-livros.html', {'livro':livro})


def Promocoes(request):
       
        return render(request, 'enter/promocoes.html', {})

def Cadastro(request):
        form = UserModelForm(request.POST or None)
        if request.method == 'POST':
                if form.is_valid():
                        form.save()
                else:
                        form = UserModelForm()
        return render(request, 'enter/idex-cadastro-de-usuario.html', {'form':form})
        
                
    
                 
                        
        
                
    




