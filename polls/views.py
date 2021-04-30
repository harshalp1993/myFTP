from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .models import *
from .tables import *
from .filters import *
from django.views.generic.edit import DeleteView
from urllib.parse import unquote_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from django.urls import reverse_lazy
from .forms import culture_info_form, samples_form, molecular_order_form, passages_form,  freezing_form
import pandas as pd 
import xlrd



get = {'userName': '%D5%AD%97%D7%FCf%B6_%A1%91s%B8%84%A4%F0%3E'}

username_hash = unquote_to_bytes(get['userName'])

key = b'QRiyMu5gNZMrhQKdEN9aD33PfXamrjUK'
iv = b'1535947594751664'

cipher = AES.new(key, AES.MODE_CBC, iv)



def index(request):
    queryset = samples.objects.all() #.filter(order_date = '2020-11-16')
    data = request.GET
    table_filter = samples_filter(data,queryset)
    table_name = samples.__name__
    table = samples_table(table_filter.qs)
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/index.html"
    context = {'table': table, 'filter': table_filter, 'table_name': table_name}
    return render(request, template, context)

def edit_samples(request, sample_id):
    sample = get_object_or_404(samples, pk = sample_id)
    form = samples_form(request.POST or None, instance=sample)
    if form.is_valid():
        form.save()
        return redirect('index')
        # redirect or show save form again
    
    context = {'culture' : sample, 'form': form}
    template = "main/editSamples.html"
    return render(request, template, context)

class samples_delete_view(DeleteView):
    model = samples
    success_url = reverse_lazy('index')
    
def cultures_view(request, sample_id):
    queryset = culture_info.objects.filter(sample_id__sample_id = sample_id)
    data = request.GET
    table_filter = cultures_filter(data,queryset)
    table_name = culture_info.__name__
    sample_name = samples.objects.get(pk = sample_id)
    table = cultures_table(table_filter.qs)
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/culturesView.html"
    context = {'table': table, 'filter': table_filter, 'table_name': table_name, 'sample_name': sample_name}
    return render(request, template, context)


def cultures_all(request):
    queryset = culture_info.objects.all()
    data = request.GET
    table_filter = cultures_filter(data,queryset)
    table_name = culture_info.__name__
    table = cultures_table(queryset)
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/culturesAll.html"
    context = {'table': table,  'filter': table_filter,'table_name': table_name}
    return render(request, template, context)


def edit_culture(request, sample_id):
    culture = get_object_or_404(culture_info, pk = sample_id)
    form = culture_info_form(request.POST or None, instance=culture)
    if form.is_valid():
        return redirect('cultures_view', sample_id=form.cleaned_data['sample_id'].sample_id)
        form.save()
        # redirect or show save form again
    
    context = {'culture' : culture, 'form': form}
    template = "main/edit_culture.html"
    return render(request, template, context)

def add_culture(request):
    form = culture_info_form(request.POST or None)
    # form.instance.sample_id = form.cleaned_data['sample_name'].sample_id
    if form.is_valid():
        form.save()
        return redirect('cultures_view', sample_id=form.cleaned_data['sample_id'].sample_id)
        # redirect or show save form again
    
    context = {'form': form}
    template = "main/edit_culture.html"
    return render(request, template, context)

def add_sample(request):
    form = samples_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index',)
        # redirect or show save form again
    
    context = {'form': form}
    template = "main/samples-form.html"
    return render(request, template, context)


def molecular_order(request, subtype_id):
    queryset = molecular_order.objects.filter(subtype_id = subtype_id)
    data = request.GET
    table_name = molecular_order.__name__
    culture_info_object = get_object_or_404(culture_info, pk = subtype_id)
    sample_name = culture_info_object.sample_id.sample_name
    table = molecular_order_table(molecular_order.objects.filter(subtype_id=subtype_id))
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/molecularorder.html"
    context = {'table': table, 'table_name': table_name,'sample_name': sample_name}
    return render(request, template, context)

def add_molecular_order(request):
    form = molecular_order_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('molecular_order', subtype_id=form.cleaned_data['subtype_id'].subtype_id)
        # redirect or show save form again
        # redirect or show save form again
    
    context = {'form': form}
    template = "main/molecularorder-form.html"
    return render(request, template, context)

def edit_molecular_order(request, subtype_id):
    mo = get_object_or_404(molecular_order, pk = subtype_id)
    form = samples_form(request.POST or None, instance=mo)
    if form.is_valid():
        form.save()
        return redirect('molecular_order')
        # redirect or show save form again
    
    context = {'culture' : mo, 'form': form}
    template = "main/editSamples.html"
    return render(request, template, context)


def passages(request, subtype_id):
    queryset = processing.objects.filter(subtype_id = subtype_id)
    data = request.GET
    table_name = processing.__name__
    culture_info_object = get_object_or_404(culture_info, pk = subtype_id)
    sample_name = culture_info_object.sample_id.sample_name
    table = processing_table(queryset)
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/passages.html"
    context = {'table': table,  'table_name': table_name, 'sample_name': sample_name}
    return render(request, template, context)


def passages_all(request):
    queryset = processing.objects.all()
    data = request.GET
    table_filter = cultures_filter(data,queryset)
    table_name = processing.__name__
    table = processing_table(queryset)
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/passages.html"
    context = {'table': table,'filter':table_filter,  'table_name': table_name}
    return render(request, template, context)

def add_passages(request):
    form = passages_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('passages', subtype_id=form.cleaned_data['subtype_id'].subtype_id)
        # redirect or show save form again
        # redirect or show save form again
    
    context = {'form': form}
    template = "main/passages-form.html"
    return render(request, template, context)

def edit_passages(request, subtype_id):
    passage = get_object_or_404(processing, pk = subtype_id)
    form = passages_form(request.POST or None, instance=passage)
    if form.is_valid():
        form.save()
        return redirect('pasages_all')
        # redirect or show save form again
    
    context = {'culture' : passage, 'form': form}
    template = "main/editPassages.html"
    return render(request, template, context)

def freezing_time(request, sample_id):
    queryset = freezing.objects.filter(sample_id = sample_id)
    data = request.GET
    table_name = freezing.__name__
    freezing_info_object = get_object_or_404(samples, pk = sample_id)
    sample_name = freezing_info_object.sample_id
    table = freezing_table(queryset)
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/freezing.html"
    context = {'table': table,  'table_name': table_name, 'sample_name': sample_name}
    return render(request, template, context)

def freezing_all(request):
    queryset = freezing.objects.all()
    data = request.GET
    table_filter = freezing_filter(data,queryset)
    table_name = freezing.__name__
    table = freezing_table(queryset)
    paginate = {'per_page': 10, 'page': 1}
    RequestConfig(request,paginate).configure(table)
    template = "main/freezing.html"
    context = {'table': table,'filter':table_filter,  'table_name': table_name}
    return render(request, template, context)

def add_freezing(request):
    form = freezing_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('freezing', processing_id=form.cleaned_data['freezing_id'].freezing_id)
        # redirect or show save form again
        # redirect or show save form again
    
    context = {'form': form}
    template = "main/freezing-form.html"
    return render(request, template, context)


def edit_freezing(request, sample_id):
    freezing = get_object_or_404(freezing, pk = sample_id)
    form = freezing_form(request.POST or None, instance=freezing)
    if form.is_valid():
        form.save()
        return redirect('freezing')
        # redirect or show save form again
    
    context = {'culture' : freezing, 'form': form}
    template = "main/editFreezing.html"
    return render(request, template, context)

class culture_info_delete(DeleteView):
    model = culture_info
    success_url = reverse_lazy("index")

def sample_full_detail_view(request, sample_id):
    sample = samples.objects.get(sample_id = sample_id)
    cultures = culture_info.objects.filter(sample_id = sample)
    culture_ids = list(culture_info.objects.filter(sample_id = sample).values_list('subtype_id'))
    processings = processing.objects.filter(subtype_id__in = culture_ids)
        
    context = {
        'sample': sample,
        'sample_table':samples_table(samples.objects.filter(sample_id = sample_id)),
        'culture_table': cultures_table(cultures),
        'processing_table': processing_table(processings),
    }
    return render(request, "main/sample_full_detail.html", context)