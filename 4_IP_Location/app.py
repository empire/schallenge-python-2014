from lib.geoipserverice import get_geo_ip
import logging


__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

do_log = False
if do_log:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)

print get_geo_ip('4.2.2.4')