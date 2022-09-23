from django.test import TestCase, Client
from django.urls import reverse, resolve
from user.views import cadastro

class CadastroTest(TestCase):
    def cliente_logado(self):
        client = Client()
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
            'senha': 'a',
        }
        client.post(reverse('valida_cadastro'), data)
        client.post(reverse('valida_login'), {'login': 'a@a', 'senha':'a'})
        return client

    def test_cadastro_view_function_is_correct(self):
        view = resolve(reverse('cadastro'))
        self.assertIs(view.func, cadastro)
    
    def test_cadastro_view_returns_status_code_200(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_cadastro_view_loads_correct_template(self):
        response = self.client.get(reverse('cadastro'))
        self.assertTemplateUsed(response, 'user/cadastro.html')
    
    def test_cadastro_view_redirect_correct_template_when_is_logged(self):
        client = self.cliente_logado()
        response = client.get(reverse('cadastro'))
        self.assertRedirects(response, reverse('home'))
    
    def test_cadastro_view_content_when_user_not_logged(self):
        response = self.client.get(reverse('cadastro'))
        self.assertIn('<title>Cadastro</title>', response.content.decode('utf-8'))
        self.assertIn('Cadastro', response.content.decode('utf-8'))
        self.assertIn('Nome', response.content.decode('utf-8'))
        self.assertIn('Email', response.content.decode('utf-8'))