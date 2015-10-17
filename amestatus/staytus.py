__author__ = 'masted'

import urllib2
import json

from amestatus.core import StatusSite


def staytus_site(c):
    """
    Simple factory to create StaytusServiceSite which use Staytus V1 Protocol.

    :param c: site configuration, must contain 'url', 'token', 'service-perma-link' field
    :return: configured staytus service site
    """
    return StaytusServiceSite(StaytusClientV1(c['url'], c['token'], c['secret']), c['service-perma-link'])


class StaytusClientV1:

    def __init__(self, api_root, api_token, api_secret):

        self._api_root = api_root
        self._api_token = api_token
        self._api_secret = api_secret

    def retrieve_status_of(self, service_name):
        return self._staytus_services_request("info", {'service': service_name})['data']['status']['permalink']

    def set_status_of(self, service_name, status_name):
        self._staytus_services_request('set_status', {'service': service_name, 'status': status_name})

    def _staytus_services_request(self, location, data):

        req = urllib2.Request(self._api_root + "/api/v1/services/" + location)
        req.add_header('X-Auth-Token', self._api_token)
        req.add_header('X-Auth-Secret', self._api_secret)
        req.add_header('Content-Type', 'application/json')
        res = urllib2.urlopen(req, json.dumps(data))

        return json.loads(res.read())


class StaytusServiceSite(StatusSite):

    def __init__(self, staytus, service_perma_link):
        self._service_perma_link = service_perma_link
        self._staytus = staytus
        self._state = None

    def in_state(self, state):
        self.__state() in state

    def to_state(self, state):
        if self.__state() != state:
            self._staytus.set_status_of(self._service_perma_link, state)

    def __state(self):
        if self._state is None:
            self._state = self._staytus.retrieve_status_of(self._service_perma_link)
        return self._state

