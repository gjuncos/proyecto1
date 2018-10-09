from django.conf.urls import include, url
from app.whatsapp.views import index, contactos_list, contactos_list_enviar


urlpatterns = [
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^listar$', contactos_list, name='index' ),
    url(r'^enviar$', contactos_list_enviar, name='enviar' ),
]
