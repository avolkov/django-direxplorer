from django.conf.urls.defaults import *

import re

#file_pattern = "[a-zA-Z0-9/-_. '-\%]+"
file_pattern = "[\S ]+"
urlpatterns = patterns('django-direxplorer.views',
    (r'^$','explore'),
    (r'^%s/zip$' % file_pattern, 'zip'),
    (r'^%s/raw$' % file_pattern, 'raw'),
    (r'^%s$' % file_pattern, 'explore'),
)