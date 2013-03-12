from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'demo.views.home', name='home'),
    url(r'^post/(\d)/$', 'demo.views.post', name='post'),
    url(r'^$', 'demo.views.template', name='template'),
    url(r'^acerca/$', 'demo.views.acerca', name='acerca'),
    url(r'^agregar/$', 'demo.views.agregar', name='agregar'),
    
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
