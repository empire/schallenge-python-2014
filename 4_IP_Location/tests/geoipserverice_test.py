from urllib2 import URLError
from lib.geoipserverice import get_geo_ip
from mock import patch, Mock, MagicMock
from socket import timeout

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

@patch('lib.geoipserverice.Client')
def test_get_geo_ip_timeout(Client_mock):
    Client_mock.get_soap_client_service.side_effect = timeout
    result = get_geo_ip('1.2.3.4')
    Client_mock.get_soap_client_service.assert_called_once()
    assert None == result

@patch('lib.geoipserverice.Client')
def test_get_geo_ip_url_error(Client_mock):
    Client_mock.get_soap_client_service.side_effect = URLError('')
    result = get_geo_ip('1.2.3.4')
    Client_mock.get_soap_client_service.assert_called_once()
    assert None == result

@patch('lib.geoipserverice.Client')
def test_get_geo_ip_url_error(Client_mock):
    Client_mock.get_soap_client_service.return_value = service = MagicMock()
    service.GetGeoIP.return_value = geo_ip = Mock()
    geo_ip.CountryName = 'Country Name'
    print service, Client_mock

    result = get_geo_ip('1.2.3.4')

    Client_mock.get_soap_client_service.assert_called_once()
    service.GetGeoIP.assert_called_once_with('1.2.3.4')
    assert 'Country Name' == result
