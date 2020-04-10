# -*- coding=utf-8 -*-
__author__ = 'Shylock'
__time__ = '2020/03/19'

import requests
import logging
class mine:
    logging.basicConfig(level=logging.DEBUG)
    def get_user_quote(self, user=None):
        r = requests.get("http://ft1.mobile.zhaoonline.com/api/user/quota",
                     # proxies={"http": "http://127.0.0.1:8877"},
                     headers={"X-ZHAO-TEST": user}
                     )
        logging.debug(r)
        return r