import django_tables2
from django_tables2.utils import A  # alias for Accessor
from .models import *
from django import forms

class samples_table(django_tables2.Table):
    sample_id   = django_tables2.Column(linkify=('sample-full-detail', {'sample_id': A('sample_id')}))
    cultures    = django_tables2.LinkColumn('cultures_view', text='view',        args=[A('pk')])
    edit        = django_tables2.LinkColumn('edit_samples',  text='edit',        args=[A('pk')])
    freezing    = django_tables2.LinkColumn('freezing',      text='Information', args=[A('pk')])
    delete      = django_tables2.LinkColumn('delete_samples', text='Delete',      args=[A('pk')])
    class Meta:
        model = samples

class cultures_table(django_tables2.Table):

    order           = django_tables2.LinkColumn('molecular_order', text='view',     args=[A('pk')])
    passages_info   = django_tables2.LinkColumn('passages',        text='passages', args=[A('pk')])
    edit            = django_tables2.LinkColumn('editCulture',     text='edit',     args=[A('pk')])
    delete          = django_tables2.LinkColumn('delete_culture',  text='Delete',   args=[A('pk')])
    class Meta:
        model = culture_info
        #exclude = ("cell_block", "patient_consent", "DateOfConsent", "Comments",)


class molecular_order_table(django_tables2.Table):
    edit = django_tables2.LinkColumn('edit_molecular_order', text='edit', args=[A('pk')])
    class Meta:
        model = molecular_order

class processing_table(django_tables2.Table):
    edit = django_tables2.LinkColumn('edit_passages', text='edit', args=[A('pk')])
    
    class Meta:
        model = processing
        unlocalize = ("passage_date", "date_block",)
        

class freezing_table(django_tables2.Table):
    edit = django_tables2.LinkColumn('edit_freezing', text='edit', args=[A('pk')])
    class Meta:
        model = freezing
