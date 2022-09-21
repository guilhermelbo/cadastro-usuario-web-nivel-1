from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('valida_cadastro/', valida_cadastro, name='valida_cadastro'),
    path('valida_login/', valida_login, name='valida_login'),
    path('logout/', logout, name='logout'),
    path('edita_cadastro/', edita_cadastro, name='edita_cadastro'),
    path('deleta_cadastro/', deleta_cadastro, name='deleta_cadastro'),
]