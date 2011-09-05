from django.conf.urls.defaults import *


file_pattern = "[a-zA-Z0-9/-_.]+"

urlpatterns = patterns('django-direxplorer.views',
    (r'^$','explore'),
    (r'^%s/zip$' % file_pattern, 'zip'),
    (r'^%s/raw$' % file_pattern, 'raw'),
    (r'^%s$' % file_pattern, 'explore'),
)