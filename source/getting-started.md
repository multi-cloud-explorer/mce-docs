# Démarrage Rapide

## Installation

```bash
git clone https://github.com/multi-cloud-explorer/mce-django-server.git
cd mce-django-server

docker-compose up -d

# Avec le proxy treafik (mettez à jour les label pour l'entrée app
export COMPOSE_FILE=docker-compose.yml:docker-compose.traefik.yml
docker-compose up -d

# Vérifiez l'état des services
docker-compose ps

# Creez le compte administrateur
docker-compose exec app ./manage.py createsuperuser --username admin --email admin@localhost.net

# Récupérer le login/password de l'administrateur
docker-compose logs app --tail 10
```

## Intégration à votre projet Django existant

TODO..

## Evaluez la solution en toute sécurité