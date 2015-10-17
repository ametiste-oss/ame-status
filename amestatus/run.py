__author__ = 'masted'

from amestatus import services, sites, default_service, default_site


def status_sync(service_cfg, site_cfg, **ext_srv_factories, **ext_site_factories):

    __services = {}
    __services.update(services)
    __services.update(ext_srv_factories)

    __sites = {}
    __sites.update(sites)
    __sites.update(ext_site_factories)

    site = __sites[site_cfg.get('type', default_site)](site_cfg)
    service = __services[service_cfg.get('type', default_service)](service_cfg)

    # NOTE: if status-service defines service as in 'maintenance-status' state, doing nothing
    if site.in_state(site_cfg.get('maintenance-status', 'maintenance')):
        return

    calculated_state = site_cfg.get('outage-status', 'major-outage') \
        if service.is_down() else site_cfg.get('operational-status', 'operational')

    site.to_state(calculated_state)



