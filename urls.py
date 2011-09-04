from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^file_explorer/', include('file_explorer.foo.urls')),
    
    (r'^explorer/', include('file_explorer.explorer.urls')),
    #(r'explorer/', 'explorer.views.hw')
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    # Uncomment the next line to enable the admin:
    
)
