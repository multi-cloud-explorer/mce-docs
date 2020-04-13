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

mce-tasks-djq
*************

Implémentation `Django-Q`_ du worker de gestion des tâches (solution intermédiaire à `Celery`_).

Une implémentation Celery pour remplacer ce composant si vous n'êtes pas convaincu par Django-Q.

mce-django-server
*****************

Solution complète, intégrant les composants précédents dans un projet Django et prêt à l'emploi dans un docker-compose.


.. include:: links.rst