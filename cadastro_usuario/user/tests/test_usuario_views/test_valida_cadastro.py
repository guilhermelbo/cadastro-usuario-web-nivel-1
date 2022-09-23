from django.test import TestCase, Client
from django.urls import reverse, resolve
from user.views import valida_cadastro
from user.models import Usuario, Endereco
from hashlib import sha256

class ValidaCadastroTest(TestCase):
    def test_valida_cadastro_view_function_is_correct(self):
        view = resolve(reverse('valida_cadastro'))
        self.assertIs(view.func, valida_cadastro)
    
    def test_valida_cadastro_redirect_when_any_field_is_empty(self):
        response = self.client.get(reverse('valida_cadastro'))
        self.assertRedirects(response, reverse('cadastro'))
    
    def test_valida_cadastro_when_email_is_used_for_another_user(self):
        senha = sha256('a'.encode()).hexdigest()
        endereco = Endereco.objects.create(pais='a', estado='a', municipio='a', cep='11111111', rua='a', numero='1', complemento='a')
        Usuario.objects.create(nome='a', email='a@a', cpf='11111111111', pis='11111111111', senha=senha, endereco_id=endereco)

        data = {
            'nome': 'a',
            'email': 'a@a',
            'cpf': '11111111111',
            'pis': '11111111111',
            'pais': 'a',
            'estado': 'a',
            'municipio': 'a',
            'cep': '11111111',
            'rua': 'a',
            'numero': '1',
            'complemento': 'a',
            'senha': senha,
        }
        response = self.client.post(reverse('valida_cadastro'), data, follow=True)
        self.assertIn('O email já está sendo utilizado por outro usuário.', response.content.decode('utf-8'))
        self.assertRedirects(response, reverse('cadastro'))
    
    def test_valida_cadastro_when_cpf_is_used_for_another_user(self):
        senha = sha256('a'.encode()).hexdigest()
        endereco = Endereco.objects.create(pais='a', estado='a', municipio='a', cep='11111111', rua='a', numero='1', complemento='a')
        Usuario.objects.create(nome='a', email='a@a', cpf='11111111111', pis='11111111111', senha=senha, endereco_id=endereco)

        data = {
            'nome': 'a',
            'email': 'b@b',
            'cpf': '11111111111',
            'pis': '11111111111',
            'pais': 'a',
            'estado': 'a',
            'municipio': 'a',
            'cep': '11111111',
            'rua': 'a',
            'numero': '1',
            'complemento': 'a',
            'senha': senha,
        }
        response = self.client.post(reverse('valida_cadastro'), data, follow=True)
        self.assertIn('O cpf já está sendo utilizado por outro usuário.', response.content.decode('utf-8'))
        self.assertRedirects(response, reverse('cadastro'))
    
    def test_valida_cadastro_when_pis_is_used_for_another_user(self):
        senha = sha256('a'.encode()).hexdigest()
        endereco = Endereco.objects.create(pais='a', estado='a', municipio='a', cep='11111111', rua='a', numero='1', complemento='a')
        Usuario.objects.create(nome='a', email='a@a', cpf='11111111111', pis='22222222222', senha=senha, endereco_id=endereco)

        data = {
            'nome': 'a',
            'email': 'b@b',
            'cpf': '22222222222',
            'pis': '22222222222',
            'pais': 'a',
            'estado': 'a',
            'municipio': 'a',
            'cep': '11111111',
            'rua': 'a',
            'numero': '1',
            'complemento': 'a',
            'senha': senha,
        }
        response = self.client.post(reverse('valida_cadastro'), data, follow=True)
        self.assertIn('O pis já está sendo utilizado por outro usuário.', response.content.decode('utf-8'))
        self.assertRedirects(response, reverse('cadastro'))