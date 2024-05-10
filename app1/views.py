from django.shortcuts import render, HttpResponse, redirect, render
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .certificate_generate import generate_certificate_nr20

# Create your views here.
@login_required(login_url='')
def HomePage(request):
    return render (request, 'home.html', {'username': request.user})

#@login_required(login_url='')
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        print("Salvou!!!")
        if User.objects.filter(username=uname):
            messages.error(request, "O nome de Usuario já existe! Tente outro.")
            return redirect('signup')

        elif User.objects.filter(email=email):
            messages.error(request, "Email já registrado!")
        
        elif pass1 != pass2:
            messages.error(request, "Senhas não são identicas")
    
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass2,
                                   first_name=first_name,
                                   last_name=last_name)
            
            #! Somente para ter uma confimação melhor, estou printando no terminal os dados
            print(f"Nome: {uname},\n"
                f"Email: {email},\n"
                f"Senha: {pass2},\n"
                f"Primeiro Nome: {first_name},\n"
                f"Último Nome: {last_name}")



            my_user.save()
            request.session['last_name'] = last_name
            return redirect('login')

    return render (request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('pass')
        
        # Verificar se o campo de entrada é um email ou um nome de usuário
        if '@' in username_or_email:
            # Se o campo de entrada contém '@', então é um email
            kwargs = {'email': username_or_email}
        else:
            # Caso contrário, é um nome de usuário
            kwargs = {'username': username_or_email}
        
        user = authenticate(request, **kwargs, password=password)
        
        if user is not None:
            if user.is_superuser:
                # Redirecionar o superadmin para a página de administração
                return redirect('signup/')
            else:
                login(request, user)
                return redirect('home')  # Redirecionar usuário normal para a página inicial
        else:
            messages.error(request, "Nome de Usuário ou Senha está incorreto!")
            return redirect('login')  # Redirecionar de volta para a página de login em caso de erro

    return render(request, 'login.html')


@login_required(login_url='')
def LogoutPage(request):
    logout(request)
    return redirect ('login')

 #path dos Cursos-Motorista
def DriverCourses(request):
    return  render(request, "cursos/cursos-motorista.html")

def DriverCourses_nr20(request):
    #return  generate_certificate_nr20(request)
    return  render(request, "cursos/cursos-motorista/curso-nr20.html")

#def generate_certificate_nr20(request):
#final-path dos Cursos-Motorista

def SSMACourses(request):
    return  render(request, "cursos/cursos-ssma.html")

def RHCourses(request):
    return  render(request, "cursos/cursos-rh.html")

def MaintenanceCourses(request):
    return render(request, "cursos/cursos-manutencao.html")

def OperationCourses(request):
   return render(request, "cursos/cursos-operacao.html") 

def FinancialCourses(request):
    return render(request, "cursos/cursos-financeiro.html") 

def MonitoringCourses(request):
    return render(request, "cursos/cursos-monitoramento.html") 

def ConfirmNr20Curse(request):
    return render(request, 'cursos/cursos-motorista/curso-nr20.html')
