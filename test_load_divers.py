# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import logging
import random

import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)


SERVER = 'http://127.0.0.1:8000/api/v1/'


def main():
    while True:
        logging.info('Free driver')
        requests.put(
            '%sdrivers/%d/' % (SERVER, random.randint(1, 200)),
            data=dict(
                lon=random.randint(-90, 90),
                lat=random.randint(-90, 90),
            ),
        )

        time.sleep(random.randint(1, 60))


if __name__ == '__main__':
    main()
