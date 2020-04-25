Multi-Cloud-Explorer
====================

.. warning::

    **Ne pas utiliser ce projet en production pour l'instant !!!**

**Multi-Cloud-Explorer** a pour objectif de **centraliser** l'inventaire et le suivi des changements, pour les ressources de **toutes vos souscriptions** Cloud.

**La récupération des resources se fait par plusieurs méthodes:**

- Inventaire périodique lancé à partir de l'application
- Réception des évènements par l'api REST, à partir d'une fonction serverless
- Appel manuel de l'api REST

**L'inventaire pourra être exploité par différents moyens:**

- Navigation et recherche dans l'application Web
- Bus d'évènements qui recevra tous les changements détectés
- Utilisation de l'api REST

.. toctree::
   :maxdepth: 2
   :caption: Introduction
   :glob:

   architecture
   getting-started
   integration
   state

.. toctree::
   :maxdepth: 1
   :caption: Azure

   cloud-libraries/azure

.. toctree::
   :maxdepth: 1
   :caption: VMware

   cloud-libraries/vsphere

Fonctionnalités
---------------

- \[x\] Inventaire automatique des resources
- \[x\] Historisation des changements au format `Json Patch`_
- \[ \] Push des évènements vers une queue de donnée ou un WebHook

Providers
---------

- [x] Azure
- [ ] AWS
- [ ] GCP
- [ ] VMware

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. include:: links.rst
