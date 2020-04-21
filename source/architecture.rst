Architecture
============

La solution est modulaire et hautement évolutive. Vous pouvez utiliser une partie des composants (ex: `mce-lib-azure`_) ou la totalité (ex: mce-django-server).

Composants
----------

mce-lib-azure
*************

Librairie pour parcourir toutes les ressources d'une souscription Azure.

mce-django-app
**************

Application Django que vous pouvez ajouter à un projet Django existant ou utiliser à travers le projet mce-django-server.

mce-tasks-rq
*************

Implémentation `Python RQ`_ du worker de gestion des tâches (alternative à `Celery`_).

mce-django-server
*****************

Solution complète, intégrant les composants précédents dans un projet Django et prêt à l'emploi dans un docker-compose.

mce-event-push
**************

Service d'envoi de message pour chaque changement dans l'inventaire.

Composants obsolètes
--------------------

mce-tasks-djq
*************

Implémentation `Django-Q`_ du worker de gestion des tâches (alternative à `Celery`_).

Ne convenait pas aux besoins.


.. include:: links.rst