# API Rest com Python e Django Rest Framework

Projeto desenvolvido para estudo do Django Rest Framework através do curso [API Rest com Python e Django Rest Framework](https://cursos.alura.com.br/course/django-rest-framework-construindo-apis-restful-zero) da [Alura](https://www.alura.com.br/).

## Iniciando o projeto

### Criando ambiente virtual

```
python -m venv venv
```

### Ativando ambiente virtual

```
source venv/bin/activate
```

### Iniciando o proejeto

```
django-admin startproject setup .
```

### Criando app

```
python manage.py startapp escola
```

### Relacionando as dependências do projeto

```
pip freeze > requirements.txt
```

### Instalando dependências

```
pip install -r requirements.txt
```

### Rodando o projeto

```
python manage.py runserver
```

## Models

### Estudante

```
{
    'id' : 1,
    'nome': John Doe,
    'email': john@doe.com.br,
    'cpf': 01234567890,
    'data_nascimento': '01/01/1900',
    'celular': 11999999999
}
```

### Cursos

```
{
    'id',: 1
    'codigo': 'POO',
    'descricao': 'Python Orientado a Objetos'
}
```

## Criando as migrations com base nas models existentes

```
python manage.py makemigrations
```

Após precisamos migrar com o comando:

```
python manage.py migrate
```

Desenvolvido por [Rodrigo Abreu](https://github.com/rodrigodabreu)
