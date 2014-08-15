import socket
import urllib2

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from suds.client import Client as SudsClient


def get_geo_ip(ip):
    try:
        service = Client.get_soap_client_service()
        result = service.GetGeoIP(ip)
        return result.CountryName
    except socket.timeout:
        return None
    except urllib2.URLError:
        return None


class Client:
    def __init__(self):
        pass

    __client = None
    @classmethod
    def get_soap_client_service(cls):
        if None != cls.__client:
            return cls.__client

        url = 'http://www.webservicex.net/geoipservice.asmx?wsdl'
        cls.__client = SudsClient(url)

        return cls.__client.service
