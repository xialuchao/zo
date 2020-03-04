import requests
import logging
import pytest

class TestRequest(object):

    logging.basicConfig(level=logging.INFO)

    def test_1(self):
        r = requests.get("http://www.zhaoonline.com")
        logging.info(r)
        logging.info(r.text)

    def test_pro(self):
        r = requests.get("http://www.zhaoonline.com",
                         proxies={"http":"http://127.0.0.1:8877"},
                         )
