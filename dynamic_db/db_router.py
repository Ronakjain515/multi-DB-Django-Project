
from .middleware import request_cfg

class DatabaseRouter(object):
    def _default_db(self):
        if hasattr(request_cfg, 'cfg'):
            print("request_cfg.cfg", request_cfg.cfg.get("NAME"))
            return request_cfg.cfg.get("NAME")
        else:
            return 'default'

    def db_for_read(self, model, **hints):
        return self._default_db()

    def db_for_write(self, model, **hints):
        print("request_cfg.cfg write", request_cfg.cfg)
        return self._default_db()