from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gerenciador/', include('gerenciador.foo.urls')),
    (r'^$','agenda.views.lista'), #faz com que execute a funcao index() localizada dentro de agenda/views.py
    (r'^adiciona/$','agenda.views.adiciona'),
    (r'^item/(?P<nr_item>\d+)/$','agenda.views.item'),
    (r'^remove/(?P<nr_item>\d+)/$','agenda.views.remove'),
    (r'^login/',"django.contrib.auth.views.login",{
        "template_name":"login.html"}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns +=patterns("",
        (r"^media/(?P<path>.*)$","django.views.static.serve",
            {'document_root':settings.MEDIA_ROOT}),)