from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import requests
from django.contrib import messages
import json
from .forms import LoginForm , RegisterForm
from .models import UserProfile

@csrf_exempt
def login_view(request):
    if request.method == "POST":
    
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username= email, password = password)
        
            if user is not None:
                login(request, user)
                return redirect(reverse('contas.html'))
            else:
                form.add_error(None, 'Credenciais inválidas')
            
        else:
            form = LoginForm()

        return redirect('http://localhost:9090/index.html')  
    
 
    return render(request, "conta.html", {'form': form})    


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']

            if password != password_confirm:
                form.add_error('password_confirm', 'As senhas não coincidem')
                messages.error(request, 'As senhas não coincidem.')
                return render(request, 'conta.html', {'form': form})

            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email já cadastrado')
                messages.error(request, 'Email já cadastrado.')
                return render(request, 'conta.html', {'form': form})

            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.first_name = fullname
                user.save()

                # Criar o perfil do usuário
                UserProfile.objects.create(
                    user=user,
                    telefone=request.POST.get('telefone', ''),
                    endereco=request.POST.get('endereco', ''),
                    cep=request.POST.get('cep', ''),
                    times=request.POST.get('times', 'Nenhum')
                )

                messages.success(request, 'Cadastro realizado com sucesso.')
                return redirect('http://localhost:9090/conta.html')  
        else:
            messages.error(request, 'Formulário inválido. Por favor, verifique os dados e tente novamente.')
            return render(request, 'conta.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'conta.html', {'form': form})