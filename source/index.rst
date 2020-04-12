Multi-Cloud-Explorer
====================

Multi-Cloud-Explorer a pour objectif de **centraliser** un inventaire des ressources de **toutes vos souscriptions** Cloud sur plusieurs fournisseurs.

**La récupération des resources se fait par plusieurs méthodes:**

- Inventaire périodique lancé à partir de l'application
- Réception des évènements par l'api REST, à partir d'une fonction serverless
- Appel manuel de l'api REST

**L'inventaire pourra être exploité par différents moyens:**

- Navigation et recherche dans l'application Web
- Bus d'évènements qui recevra tous les changements détectés
- Utilisation de l'api REST


.. toctree::
   :maxdepth: 1
   :glob:

   getting-started
   cloud-libraries/azure

Fonctionnalités
---------------

- [x] Inventaire automatique des resources
- [x] Historisation des changements au format [Json Patch](http://jsonpatch.com/)
- [ ] Push des évènements vers une queue de donnée ou un WebHook

Providers
---------

- [x] Azure
- [ ] AWS
- [ ] GCP

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

