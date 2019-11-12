2. Edit the ``/etc/prometheus_alertmanager_dingtalk/prometheus_alertmanager_dingtalk.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://prometheus_alertmanager_dingtalk:PROMETHEUS_ALERTMANAGER_DINGTALK_DBPASS@controller/prometheus_alertmanager_dingtalk
