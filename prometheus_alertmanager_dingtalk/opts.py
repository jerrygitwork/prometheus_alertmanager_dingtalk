from oslo_config import cfg

CONF = cfg.CONF

server = [
    cfg.StrOpt('addr',
               default='0.0.0.0',
               help=''),
    cfg.PortOpt('port',
                default=8006,
                help='port number to listen on')
]

dingtalk = [
    cfg.StrOpt('token_url',
               default='https://oapi.dingtalk.com/robot/send'),
    cfg.StrOpt('secret',
               default='349b6875c2be43c08')
]


def register_opts():
    server_group = cfg.OptGroup(name='server',
                                title="Options for http server.")
    dingtalk_group = cfg.OptGroup(name='dingtalk',
                                  title="Options for dingtalk.")

    CONF.register_group(server_group)
    CONF.register_group(dingtalk_group)

    CONF.register_opts(server, server_group)
    CONF.register_opts(dingtalk, dingtalk_group)
