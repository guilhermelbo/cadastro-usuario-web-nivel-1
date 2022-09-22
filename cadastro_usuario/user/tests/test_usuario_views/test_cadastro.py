from django.test import TestCase
from django.urls import reverse, resolve
from user.views import cadastro

class CadastroTest(TestCase):
    def test_cadastro_view_function_is_correct(self):
        view = resolve(reverse('cadastro'))
        self.assertIs(view.func, cadastro)