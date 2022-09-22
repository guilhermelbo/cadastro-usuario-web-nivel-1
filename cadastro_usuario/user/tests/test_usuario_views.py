from django.test import TestCase
from django.urls import reverse, resolve
from user import views

class UsuarioViewsTest(TestCase):
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)

    def test_cadastro_view_function_is_correct(self):
        view = resolve(reverse('cadastro'))
        self.assertIs(view.func, views.cadastro)
    
    def test_valida_cadastro_view_function_is_correct(self):
        view = resolve(reverse('valida_cadastro'))
        self.assertIs(view.func, views.valida_cadastro)

    def test_valida_login_view_function_is_correct(self):
        view = resolve(reverse('valida_login'))
        self.assertIs(view.func, views.valida_login)
    
    def test_logout_view_function_is_correct(self):
        view = resolve(reverse('logout'))
        self.assertIs(view.func, views.logout)
    
    def test_edita_cadastro_view_function_is_correct(self):
        view = resolve(reverse('edita_cadastro'))
        self.assertIs(view.func, views.edita_cadastro)
    
    def test_deleta_cadastro_view_function_is_correct(self):
        view = resolve(reverse('deleta_cadastro'))
        self.assertIs(view.func, views.deleta_cadastro)
    
    def test_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_view_loads_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'user/home.html')
    
    def test_home_view_context_if_user_not_logged(self):
        response = self.client.get(reverse('home'))
        context = {
            'usuario': 'visitante',
            'logado': False
        }
        for c in context:
            self.assertEqual(response.context[c], context[c])
    
    def test_home_view_content_if_user_not_logged(self):
        response = self.client.get(reverse('home'))
        self.assertIn('Olá visitante', response.content.decode('utf-8'))
