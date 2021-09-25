# -*- coding: utf-8 -*-
"""
Descrition
"""
__author__ = 'maxdob'
__date__ = '25.09.21'
__time__ = '21:32'
__version__ = '0.1'

# from threading import Thread
import time
from exonum_client.api import ServiceApi
from settings import Exonum

class BaseService():
    def __init__(self, name: str, track_entities: list):
        # super().__init__()
        self._name = name
        self._track_entities = track_entities
        self.__service = ServiceApi(service_name = Exonum._service_name, hostname = Exonum._host,
                                    port = Exonum._port, schema=Exonum._schema)
        # self.__service.service_endpoint()

    def run(self):
        while True:
            self.__main_loop()
            time.sleep(60*5)

    def __main_loop(self):

        for entity in self._track_entities:
            data = self.__service.get_service("v1/{0}/list?pub_key={1}".format(entity,Exonum._public_key))
            print (data.request)
            if data:
                print(data.json())

