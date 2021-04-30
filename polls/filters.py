import django_filters
from django_filters import ChoiceFilter, CharFilter
from .models import *

class samples_filter(django_filters.FilterSet):

    ORGAN_CHOICES = [('Pleura', 'Pleura'), 
    ('Pancreas', 'Pancreas'),
    ('Soft tissue', 'Soft tissue'),
    ('Peritoneum', 'Peritoneum'),
    ('Lung', 'Lung'),
    ('Liver', 'Liver'),
    ('Sinunasal', 'Sinunasal'),
    ('Unknown', 'Unknown'),
    ('Colon', 'Colon'),
    ('Adrenal gland', 'Adrenal gland'),
    ('Kidney', 'Kidney'),
    ('Small intestine', 'Small intestine'),
    ('Anal', 'Anal'),
    ('Thyroid', 'Thyroid'),
    ('Lung', 'Lung'),
    ('Ovary', 'Ovary'),
    ('Peritoneum', 'Peritoneum'),
    ('Bone', 'Bone'),
    ('Rectum', 'Rectum'),
    ('Appendix', 'Appendix'),
    ('Salivary Gland', 'Salivary Gland'),
    ('Testis', 'Testis'),
    ('Stomach', 'Stomach'),
    ('Thymus', 'Thymus'),
    ('Mediastinum', 'Mediastinum'),
    ('Cervix', 'Cervix'),
    ('Brain', 'Brain'),
    ('Cat', 'Cat'),
    ('Dog', 'Dog'),
    ('Mouse', 'Mouse'),
    ('Prostate', 'Prostate'),
    ('Breast', 'Prostate'),
    ('Esophagus', 'Esophagus'),
    ('Cell line', 'Cell line')]

    TUMOR_CHOICES = [('CUP', 'CUP'),
    ('PDAC', 'PDAC'),
    ('Sarcoma', 'Sarcoma'),
    ('CRC', 'CRC'),
    ('SCC', 'SCC'),
    ('HCC', 'HCC'),
    ('Melanoma', 'Melanoma'),
    ('Carcinoma', 'Carcinoma'),
    ('Tumor', 'Tumor'),
    ('Ampullary CA', 'Ampullary CA'),
    ('NTRK', 'NTRK'),
    ('CCC', 'CCC'),
    ('Esophagus CA', 'Eshophagus CA'),
    ('Papillary CA', 'Papillary CA'),
    ('Clearcell CA', 'Clearcell CA'),
    ('Appendix CA', 'Appendix CA'),
    ('Serous', 'Serous'),
    ('Mesothelioma', 'Mesothelioma'),
    ('NET', 'NET'),
    ('Breast CA', 'Breast CA'),
    ('Adenocarcinoma', 'Adenocarcinoma'),
    ('Germ cell tumor', 'Germ cell tumor'),
    ('MMMT', 'MMMT'),
    ('Seminoma', 'Seminoma'),
    ('Thymom', 'Thymom'),
    ('MagenCA', 'MagenCA'),
    ('Acinar cell Carcinoma', 'Acinar cell Carcinoma'),
    ('Adenoma', 'Adenoma'),
    ('Liver', 'Liver'),
    ('SCLC', 'SCLC'),
    ('Lymphoma', 'Lymphoma'),
    ('Angio Sarcoma', 'Angio Sarcoma'),
    ('Baby', 'Baby'),
    ('Baby Sarcoma', 'Baby Sarcoma'),
    ('Lung Carcinoma', 'Lung Carcinoma'),
    ('Chondrosarcoma', 'Chondrosarcoma'),
    ('HCA', 'HCA'),
    ('Giant cell tumor 2D', 'Giant cell tumor 2D'),
    ('IMT 2D', 'IMT 2D'),]


    organ = ChoiceFilter(choices =  ORGAN_CHOICES, label="Organ")
    tumor_type = ChoiceFilter(choices = TUMOR_CHOICES, label="Tumor Type")
    sample_name = CharFilter(label="Sample Name")


    class Meta:
        model = samples
        fields = ('sample_name', 'organ', 'tumor_type')
        

class cultures_filter(django_filters.FilterSet):
    class Meta:
        model = culture_info
        fields = {'subtype_id':['icontains'], 'subtype_info':['icontains'], 'passage':['icontains']}

class molecular_order_filter(django_filters.FilterSet):
    class Meta:
        model = molecular_order
        fields = {'molecular_order_id':['icontains']}

class freezing_filter(django_filters.FilterSet):
    class Meta:
        model = freezing
        fields = {'freezing_id':['icontains']}
 
