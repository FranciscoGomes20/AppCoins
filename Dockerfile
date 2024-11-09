# Use uma imagem leve de Python
FROM python:3.12.4-alpine3.20

# Definindo variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar as dependências do PostgreSQL e compilers
RUN apk add --no-cache postgresql-dev gcc musl-dev

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /AppCoins

# Copie os arquivos de requerimento para instalar dependências
COPY requirements.txt /AppCoins/

# Criar um ambiente virtual e instalar as dependências
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r requirements.txt

# Copie o script wait-for-it.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Copie todo o projeto para o diretório de trabalho
COPY . .

# Expõe a porta 8000 (a porta padrão do Django)
EXPOSE 8000
