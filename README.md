# AMBIENTE DE DESENVOLVIMENTO

Ambiente de desenvolvimento com Docker, Django e Postregresql

# RODANDO TESTES

Para execurtar django-pytest dentro do container:
    docker-compose run djangoapp python manage.py test -v 2

Para executar o pytest dentro do container:
    docker-compose run djangoapp pytest -v
