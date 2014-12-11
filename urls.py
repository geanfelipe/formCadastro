from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gerenciador/', include('gerenciador.foo.urls')),
    (r'^$','agenda.views.lista'), #faz com que execute a funcao index() localizada dentro de agenda/views.py
    (r'^adiciona/$','agenda.views.adiciona'),
    (r'^item/(?P<nr_item>\d+)/$','agenda.views.item'),
    (r'^remove/(?P<nr_item>\d+)/$','agenda.views.remove'),
    (r'^login/',"django.contrib.auth.views.login",{
        "template_name":"login.html"}),
    (r'^logout/','django.contrib.auth.views.logout_then_login',
        {'login_url':'/login/'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns +=patterns("",
        (r"^media/(?P<path>.*)$","django.views.static.serve",
            {'document_root':settings.MEDIA_ROOT}),)