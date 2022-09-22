from django.test import TestCase, Client
from django.urls import reverse, resolve
from user.views import home

class HomeTest(TestCase):
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

    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, home)
    
    def test_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'user/home.html')
    
    def test_home_view_context_when_user_not_logged(self):
        response = self.client.get(reverse('home'))
        context = {
            'usuario': 'visitante',
            'logado': False
        }
        for c in context:
            self.assertEqual(response.context[c], context[c])
    
    def test_home_view_content_when_user_not_logged(self):
        response = self.client.get(reverse('home'))
        self.assertIn('Olá visitante', response.content.decode('utf-8'))
    
    def test_home_view_context_when_user_is_logged(self):
        client = self.cliente_logado()
        response = client.get(reverse('home'))
        context = {
            'usuario': 'a',
            'logado': True
        }
        for c in context:
            self.assertEqual(response.context[c], context[c])

    def test_home_view_content_when_user_is_logged(self):
        client = self.cliente_logado()
        response = client.get(reverse('home'))
        self.assertIn('Olá a', response.content.decode('utf-8'))
        self.assertIn('Editar dados cadastrais', response.content.decode('utf-8'))