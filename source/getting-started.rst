Getting Started
===============

Installation
------------

.. code-block:: bash

    git clone https://github.com/multi-cloud-explorer/mce-django-server.git
    cd mce-django-server

    export COMPOSE_FILE=docker-compose.yml:docker-compose.prod.yml
    docker-compose up -d --build

    # Vérifiez l'état des services
    docker-compose ps

    # Creez le compte administrateur
    docker-compose exec app ./manage.py createsuperuser --username admin --email admin@localhost.net

    # Récupérer le login/password de l'administrateur
    docker-compose logs app --tail 10



