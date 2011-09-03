from django.conf.urls.defaults import *

file_pattern = "[a-zA-Z0-9/-_.]+"

urlpatterns = patterns('',
    # Example:
    # (r'^file_explorer/', include('file_explorer.foo.urls')),
    (r'^$','explorer.views.hw'),
    (r'^%s/zip$' % file_pattern, 'explorer.views.zip'),
    (r'^%s/raw$' % file_pattern, 'explorer.views.raw'),
    (r'^%s$' % file_pattern, 'explorer.views.explore'),
)