from django.test import TestCase
from django.urls import reverse, resolve
from user.views import edita_cadastro

class EditaCadastroTest(TestCase):
    def test_edita_cadastro_view_function_is_correct(self):
        view = resolve(reverse('edita_cadastro'))
        self.assertIs(view.func, edita_cadastro)