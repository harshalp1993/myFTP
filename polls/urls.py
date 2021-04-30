from django.urls import path
from django.urls import re_path 
from django.conf.urls import url
from . import views
from django.contrib import admin
from polls.views import *
from django.views.generic import TemplateView
from .views import DeleteView
from .views import samples_delete_view


urlpatterns = [

    path('freezing_all/', views.freezing_all, name='freezing_all'),
    path('', views.index, name='index'),
    path('<str:pk>/delete_samples/', views.samples_delete_view.as_view(), name='delete_samples'),
    path('cultures_all/', views.cultures_all, name = 'cultures_all'),
    path('<str:sample_id>/cultures_view/', views.cultures_view, name='cultures_view'),
    path('add_sample/', views.add_sample, name='add_sample'),
    path('passages_all/', views.passages_all, name='pasages_all'),
    path('index', views.index, name='index'),
    path('<str:sample_id>/edit_samples/', views.edit_samples, name='edit_samples'),
    path('<str:sample_id>/edit_culture/', views.edit_culture, name='editCulture'),
    path('<str:pk>/delete_culture/', views.culture_info_delete.as_view(), name='delete_culture'),
    path('add_culture/', views.add_culture, name='add_culture'),
    path('<str:subtype_id>/molecular_order/', views.molecular_order, name='molecular_order'),
    path('add_molecular_order/', views.add_molecular_order, name='add_molecular_order'),
    path('<str:subtype_id>/edit_molecular_order/', views.edit_molecular_order, name='edit_molecular_order'),
    path('<str:subtype_id>/passages/', views.passages, name='passages'),
    path('add_passages/', views.add_passages, name='add_passages'),
    path('<str:subtype_id>/edit_passages/', views.edit_passages, name='edit_passages'),
    path('<str:sample_id>/freezing/', views.freezing_time, name='freezing'),
    path('add_freezing/', views.add_freezing, name='add_freezing'),
    path('<str:sample_id>/edit_freezing/', views.edit_freezing, name='edit_freezing'),
    path('<str:sample_id>/full-detail/',views.sample_full_detail_view,name='sample-full-detail'),
    path('cellbiobank/', TemplateView.as_view(template_name='/polls/cellbiobank.html'), name='cellbiobank'),
]




