__author__ = 'masted'

import urllib
import json

from amestatus.core import Service


def htt_spring_boot(c):
    """
    Simple factory to create HttpSpringBootService.

    :param c: service configuration, must contain service 'url'.
    :return: configured service
    """
    return HttpSpringBootService(c['url'])


class HttpSpringBootService(Service):

    def __init__(self, service_url):

        self._url = service_url
        self._health_url = service_url + "/health"

    def is_up(self):

        is_up = True

        try:
            data = json.loads(urllib.urlopen(self._health_url).read())
        except Exception:
            is_up = False

        if is_up and data['status'] != 'UP':
            is_up = False

        return is_up
