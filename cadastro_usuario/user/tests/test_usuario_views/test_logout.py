from django.test import TestCase
from django.urls import reverse, resolve
from user.views import logout

class LogoutTest(TestCase):
    def test_logout_view_function_is_correct(self):
        view = resolve(reverse('logout'))
        self.assertIs(view.func, logout)