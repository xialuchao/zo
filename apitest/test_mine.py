# -*- coding=utf-8 -*-
__author__ = 'Shylock'
__time__ = '2020/03/19'

import logging

import requests

from apitest.mine import mine


class TestMine(object):
    logging.basicConfig(level=logging.DEBUG)

    def test_user_quote(self):
        # r = requests.get("http://ft1.mobile.zhaoonline.com/api/user/quota",
        #                  proxies={"http":"http://127.0.0.1:8877"},
        #                  headers={"X-ZHAO-TEST":"1000010"}
        #                  ).json()
        # logging.debug(r)
        logging.debug(mine.get_user_quote(1000010).text)