from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
file_pattern = "[a-zA-Z0-9/-_.]+"

urlpatterns = patterns('',
    # Example:
    # (r'^file_explorer/', include('file_explorer.foo.urls')),
    (r'^$','explorer.views.hw'),
    (r'^%s/zip$' % file_pattern, 'explorer.views.zip'),
    (r'^%s/raw$' % file_pattern, 'explorer.views.raw'),
    (r'^%s$' % file_pattern, 'explorer.views.explore')
    #(r'^explorer/', include('file_explorer.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)