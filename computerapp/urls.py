from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path ( 'machines/',views.machine_list_view, name='machines'),
    path ( 'personnels/',views.perso_list_view, name='personnels'),
    path ( 'ifra/',views.infra_list_view, name='infra'),
    path ( 'add-machine',views.machine_add_form, name='add-machine'),
    path ( 'partenaire/',views.partenaires_list_view, name='partenaire'),

]







