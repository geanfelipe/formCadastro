from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gerenciador/', include('gerenciador.foo.urls')),
    (r'^$','agenda.views.lista'), #faz com que execute a funcao index() localizada dentro de agenda/views.py
    (r'^adiciona/$','agenda.views.adiciona'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

)
