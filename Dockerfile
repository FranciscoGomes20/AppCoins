# Use uma imagem leve de Python
FROM python:3.12.4-alpine3.20

# Variáveis de ambiente para otimizar o comportamento do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do contêiner
WORKDIR /AppCoins

# Instalar dependências de compilação
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    libffi-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    linux-headers

# Copie os arquivos de requerimento para instalar dependências
COPY requirements.txt .

# Criar ambiente virtual e instalar dependências Python
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r requirements.txt

# Copie todo o projeto para o diretório de trabalho
COPY . .

# Defina o caminho para o Python e pip no ambiente virtual
ENV PATH="/py/bin:$PATH"

# Executa as migrações e inicializa o servidor Django ao iniciar o contêiner
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# Expõe a porta 8000 (a porta padrão do Django)
EXPOSE 8000

