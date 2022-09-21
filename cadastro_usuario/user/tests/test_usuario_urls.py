from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class UsuarioUrlsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('home')
        self.assertEqual(url, '/')

    def test_cadastro_url_is_correct(self):
        url = reverse('cadastro')
        self.assertEqual(url, '/cadastro/')
    
    def test_valida_cadastro_url_is_correct(self):
        url = reverse('valida_cadastro')
        self.assertEqual(url, '/valida_cadastro/')

    def test_valida_login_url_is_correct(self):
        url = reverse('valida_login')
        self.assertEqual(url, '/valida_login/')

    def test_logout_url_is_correct(self):
        url = reverse('logout')
        self.assertEqual(url, '/logout/')

    def test_edita_cadastro_url_is_correct(self):
        url = reverse('edita_cadastro')
        self.assertEqual(url, '/edita_cadastro/')

    def test_deleta_cadastro_url_is_correct(self):
        url = reverse('deleta_cadastro')
        self.assertEqual(url, '/deleta_cadastro/')