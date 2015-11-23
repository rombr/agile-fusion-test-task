# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import logging
import random
from datetime import timedelta, datetime

import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)


SERVER = 'http://127.0.0.1:8000/api/v1/'


def main():
    while True:
        logging.info('New client')
        requests.post(
            '%sorders/' % SERVER,
            data=dict(
                client=random.randint(1, 1000),
                lon=random.randint(-90, 90),
                lat=random.randint(-90, 90),
                time=random.choice([
                    None,
                    datetime.now() + timedelta(minutes=2),
                ]),
            ),
        )

        time.sleep(random.randint(1, 10))


if __name__ == '__main__':
    main()
