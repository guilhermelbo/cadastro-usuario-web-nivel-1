from django.test import TestCase
from django.urls import reverse, resolve
from user.views import valida_cadastro

class ValidaCadastroTest(TestCase):
    def test_valida_cadastro_view_function_is_correct(self):
        view = resolve(reverse('valida_cadastro'))
        self.assertIs(view.func, valida_cadastro)