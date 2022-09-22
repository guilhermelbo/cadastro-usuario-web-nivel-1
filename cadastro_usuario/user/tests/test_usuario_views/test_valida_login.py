from django.test import TestCase
from django.urls import reverse, resolve
from user.views import valida_login

class ValidaLoginTest(TestCase):
    def test_valida_login_view_function_is_correct(self):
        view = resolve(reverse('valida_login'))
        self.assertIs(view.func, valida_login)