from django.contrib import admin
from django.urls import path, include
from .views import hello
from .views import hello2,tipopremio
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as client_urls
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tipopremio, name='home'),
    path('login/',  LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.logout, name='logout'),
    path('hello/', hello),
    path('person/', include(client_urls)),
    path('hello/', hello2)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
