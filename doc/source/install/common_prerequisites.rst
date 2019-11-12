Prerequisites
-------------

Before you install and configure the prometheus_alertmanager_dingtalk service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``prometheus_alertmanager_dingtalk`` database:

     .. code-block:: none

        CREATE DATABASE prometheus_alertmanager_dingtalk;

   * Grant proper access to the ``prometheus_alertmanager_dingtalk`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON prometheus_alertmanager_dingtalk.* TO 'prometheus_alertmanager_dingtalk'@'localhost' \
          IDENTIFIED BY 'PROMETHEUS_ALERTMANAGER_DINGTALK_DBPASS';
        GRANT ALL PRIVILEGES ON prometheus_alertmanager_dingtalk.* TO 'prometheus_alertmanager_dingtalk'@'%' \
          IDENTIFIED BY 'PROMETHEUS_ALERTMANAGER_DINGTALK_DBPASS';

     Replace ``PROMETHEUS_ALERTMANAGER_DINGTALK_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``prometheus_alertmanager_dingtalk`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt prometheus_alertmanager_dingtalk

   * Add the ``admin`` role to the ``prometheus_alertmanager_dingtalk`` user:

     .. code-block:: console

        $ openstack role add --project service --user prometheus_alertmanager_dingtalk admin

   * Create the prometheus_alertmanager_dingtalk service entities:

     .. code-block:: console

        $ openstack service create --name prometheus_alertmanager_dingtalk --description "prometheus_alertmanager_dingtalk" prometheus_alertmanager_dingtalk

#. Create the prometheus_alertmanager_dingtalk service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        prometheus_alertmanager_dingtalk public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        prometheus_alertmanager_dingtalk internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        prometheus_alertmanager_dingtalk admin http://controller:XXXX/vY/%\(tenant_id\)s
