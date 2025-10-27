#!/bin/bash

# Este script garante que as migrações sejam aplicadas antes de iniciar o servidor.

# 1. Faz as migrações (cria novos arquivos, se houver alterações no modelo)
echo "-> Verificando e criando migrações..."
python manage.py makemigrations

# 2. Aplica as migrações ao banco de dados
echo "-> Aplicando migrações ao banco de dados..."
python manage.py migrate

# 3. Inicia o servidor da aplicação (o comando original)
echo "-> Iniciando o servidor Django..."
exec python manage.py runserver 0.0.0.0:8000