# Introduction

Ame-status is toolkit to communicate with _status sites_ like [Staytus](https://github.com/adamcooke/staytus).
Toolkit provides framework to sync your _services state_ and _status_ on a site, connectors to popular service platforms
([Spring Boot](https://github.com/spring-projects/spring-boot), etc.) and _status sites_ implementations.

# At a Glance

Amestatus library primarily designed to provide easy way to build status update middleware, library does not
dictate the way of how middleware should be build or what is must be. 

For example, easiest way to build such kind of middleware using Amestatus library is python script 
that could be used, for example, as crontab task

```python
#!/usr/bin/env python

from amestatus import status_sync

if __name__ == '__main__':

  status_sync(
      {
         'url': "http://service.host.local",
         'type': 'http-spring-boot'
      },
      {
         'url': 'http://status.site.host.local',
         'type': 'staytus-v1',
         
         'token': "88e8-b6c603bb9ccb",
         'secret': "NmzEfSzrzltCK",
         
         'service-perma-link': 'service-local',

         'outage-status': 'major-outage',
         'maintenance-status': 'maintenance'
      }
  )
  
```

See wiki pages ( _atm under construction, feel free to ask help via issues) and sections below for 
setup details and concrete services and sites configuration options.

# Installation

Amestatus library distributed as python egg via github repository. So you could install it using pip in standard way.

To get last master snapshot egg

```
sudo pip install git+https://github.com/ametiste-oss/ame-status.git
```

To get last stable snapshot egg

```
sudo pip install git+https://github.com/ametiste-oss/ame-status.git@stable
```

To get concrete version egg

```
sudo pip install git+https://github.com/ametiste-oss/ame-status.git@v1.0.0
```
