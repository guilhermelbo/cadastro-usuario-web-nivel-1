from django.shortcuts import render, redirect
from .models import Usuario, Endereco
from django.contrib import messages
from hashlib import sha256

# Create your views here.
def home(request):
    context = {
        'usuario': 'visitante',
        'logado': False 
    }
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.filter(id=usuario_id)[0]
        logado = True
        context['usuario'] = usuario.nome
        context['logado'] = logado
    return render(request, 'user/home.html', context)

def cadastro(request):
    if request.session.get('usuario_id'):
        return redirect('home')
    return render(request, 'user/cadastro.html')

def valida_cadastro(request):
    novo_cadastro = True
    url_redirect = 'cadastro'

    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.filter(id=usuario_id)
        novo_cadastro = False
        url_redirect = 'edita_cadastro'

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    cpf = request.POST.get('cpf')
    pis = request.POST.get('pis')
    pais = request.POST.get('pais')
    estado = request.POST.get('estado')
    municipio = request.POST.get('municipio')
    cep = request.POST.get('cep')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')
    complemento = request.POST.get('complemento')
    senha = request.POST.get('senha')

    if(not nome or 
            not email or 
            not cpf or 
            not pis or 
            not pais or 
            not estado or 
            not municipio or
            not cep or
            not rua):
        messages.error(request, 'Campos obrigatórios não podem estar vazios.')
        return redirect(url_redirect)

    usuario_email = Usuario.objects.filter(email=email)
    if usuario_email:
        if novo_cadastro or usuario[0].id != usuario_email[0].id:
            messages.error(request, 'O email já está sendo utilizado por outro usuário.')
            return redirect(url_redirect)
        
    usuario_cpf = Usuario.objects.filter(cpf=cpf)
    if usuario_cpf:
        if novo_cadastro or usuario[0].id != usuario_cpf[0].id:
            messages.error(request, 'O cpf já está sendo utilizado por outro usuário.')
            return redirect(url_redirect)
    
    usuario_pis = Usuario.objects.filter(pis=pis)
    if usuario_pis:
        if novo_cadastro or usuario[0].id != usuario_pis[0].id:
            messages.error(request, 'O pis já está sendo utilizado por outro usuário.')
            return redirect(url_redirect)


    if len(cpf) < 11 or len(cpf) > 11:
        messages.error(request, 'O cpf precisa ter 11 dígitos.')
        return redirect(url_redirect)

    if len(pis) < 11 or len(pis) > 11:
        messages.error(request, 'O pis precisa ter 11 dígitos.')
        return redirect(url_redirect)
    
    if len(cep) < 8 or len(cep) > 8:
        messages.error(request, 'O cep precisa ter 8 dígitos.')
        return redirect(url_redirect)
    
    if numero == '':
        numero = None

    if novo_cadastro:
        try:
            senha = sha256(senha.encode()).hexdigest()
            endereco = Endereco(pais=pais, estado=estado, municipio=municipio, cep=cep, rua=rua, numero=numero, complemento=complemento)
            endereco.save()
            usuario = Usuario(nome=nome, email=email,cpf=cpf,pis=pis,senha=senha,endereco_id=endereco)
            usuario.save()
        except:
            messages.error(request, 'Erro no servidor')
            return redirect(url_redirect)

        messages.success(request, 'Usuário cadastrado com sucesso.')
    else:
        try:
            senha = sha256(senha.encode()).hexdigest()
            endereco_id = usuario[0].endereco_id.id
            endereco = Endereco.objects.filter(id=endereco_id)
            usuario.update(
                nome = nome,
                email = email,
                cpf = cpf,
                pis = pis,
                senha = senha,
            )
            endereco.update(
                pais = pais,
                estado = estado,
                municipio = municipio,
                cep = cep,
                rua = rua,
                numero = numero,
                complemento = complemento,
            )
        except:
            messages.error(request, 'Erro no servidor')
            return redirect(url_redirect)  
        messages.success(request, 'Usuário alterado com sucesso.')
    return redirect('home')

def valida_login(request):
    if request.session.get('usuario_id'):
        return redirect('home')

    login = request.POST.get('login')
    senha = request.POST.get('senha')

    if not login or not senha or len(login.strip()) == 0:
        messages.error(request, 'Usuário ou senha não podem estar vazios.')
        return redirect('home')
    
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=login).filter(senha=senha)
    if usuario:
        request.session['usuario_id'] = usuario[0].id
        return redirect('home') 

    usuario = Usuario.objects.filter(cpf=login).filter(senha=senha)
    if usuario:
        request.session['usuario_id'] = usuario[0].id
        return redirect('home')

    usuario = Usuario.objects.filter(pis=login).filter(senha=senha)
    if usuario:
        request.session['usuario_id'] = usuario[0].id
        return redirect('home')

    messages.error(request, 'Usuário ou senha incorretos.')
    return redirect('home')

def edita_cadastro(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.filter(id=usuario_id)[0]
        endereco = usuario.endereco_id
        context = {
            'nome' : usuario.nome,
            'email': usuario.email,
            'cpf': usuario.cpf,
            'pis': usuario.pis,
            'pais': endereco.pais,
            'estado': endereco.estado,
            'municipio': endereco.municipio,
            'cep': endereco.cep,
            'rua': endereco.rua,
            'numero': endereco.numero,
            'complemento': endereco.complemento,
        }
        return render(request, 'user/edita_cadastro.html', context)
    return redirect('home')

def deleta_cadastro(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.filter(id=usuario_id)
        endereco = Endereco.objects.filter(id=usuario[0].endereco_id.id)
        usuario.delete()
        endereco.delete()
        messages.success(request, 'Usuário deletado com sucesso.')
        return redirect('logout')
    return redirect('home')

def logout(request):
    request.session.flush()
    return redirect('home')