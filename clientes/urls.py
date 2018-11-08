
from django.urls import path
from .views import person_list
from .views import person_new
from .views import person_update
from .views import person_delete
from .views import tipopremio

urlpatterns = [
    path('list/', person_list, name = 'person_list'),
    path('', tipopremio, name='home'),
    path('new/', person_new, name = 'person_new'),
    path('update/<int:id>', person_update, name = 'person_update'),
    path('delete/<int:id>', person_delete, name = 'person_delete')
]