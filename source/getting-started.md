# Démarrage Rapide


## Installation avec docker-compose

```bash
git clone https://github.com/multi-cloud-explorer/mce-django-server.git
cd mce-django-server

docker-compose up -d

# Vérifiez l'état des services
docker-compose ps

# Créez le compte administrateur
docker-compose exec app ./manage.py createsuperuser \
   --username admin --email admin@localhost.net

# Récupérez le login/password de l'administrateur
docker-compose logs app --tail 10
```

## Intégration à votre projet Django existant

TODO..

## Evaluez la solution en toute sécurité
