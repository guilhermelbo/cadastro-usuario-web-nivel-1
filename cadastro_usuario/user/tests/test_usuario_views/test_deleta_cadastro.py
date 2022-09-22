from django.test import TestCase
from django.urls import reverse, resolve
from user.views import deleta_cadastro

class DeletaCadastroTest(TestCase):
    def test_deleta_cadastro_view_function_is_correct(self):
        view = resolve(reverse('deleta_cadastro'))
        self.assertIs(view.func, deleta_cadastro)