__author__ = 'masted'

from amestatus.spring import htt_spring_boot
from amestatus.staytus import staytus_site

default_service = 'http-spring-boot'
default_site = 'staytus-v1'

services = {
    'http-spring-boot': htt_spring_boot
}

sites = {
    'staytus-v1': staytus_site
}
