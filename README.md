# Cadastro de usuario nivel 1

## Link da aplicação no heroku

https://crud-nivel-1.herokuapp.com/

## Instruções 

Abra o windows powershell na pasta que deseja clonar o projeto

```bash
git clone https://github.com/guilhermelbo/cadastro-usuario-web-nivel-1
cd cadastro-usuario-web-nivel-1
python -m venv venv
.\venv\Scripts\activate
cd cadastro_usuario
pip install -r requirements.txt
```
Depois disso é necessário criar um banco de dados postgresql
e criar o arquivo .env na mesma pasta do settings.py com as seguintes variáveis de ambiente:

Exemplo:

```
SECRET_KEY=django-insecure-6q%wa9wg8$+=#jqs5z1t_x$kou9mg-p($gn1idcvl%j6a%qw1+
DEBUG=True
DATABASE_URL=postgres://postgres:123456@localhost:5432/cadastro-usuario
```

Feito isso basta executar os seguintes comandos na mesma pasta do manage.py

```bash
python manage.py migrate
python manage.py runserver
```
