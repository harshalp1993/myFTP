from django import forms

from polls.models import samples
from polls.models import culture_info
from polls.models import molecular_order
from polls.models import processing
from polls.models import freezing
import datetime

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
    ('AmpullaryCA', 'AmpullaryCA'),
    ('NTRK', 'NTRK'),
    ('CCC', 'CCC'),
    ('EsophagusCA', 'EshophagusCA'),
    ('PapillaryCA', 'PapillaryCA'),
    ('ClearcellCA', 'ClearcellCA'),
    ('AppendixCA', 'AppendixCA'),
    ('Serous', 'Serous'),
    ('Mesothelioma', 'Mesothelioma'),
    ('NET', 'NET'),
    ('BreastCA', 'BreastCA'),
    ('Adenocarcinoma', 'Adenocarcinoma'),
    ('CRC', 'CRC'),
    ('Germ cell tumor', 'Germ cell tumor'),
    ('MMMT', 'MMMT'),
    ('Seminoma', 'Seminoma'),
    ('Thymom', 'Thymom'),
    ('MagenCA', 'MagenCA'),
    ('Acinar cell Carcinoma', 'Acinar cell Carcinoma'),
    ('Adenoma', 'Adenoma'),
    ('Liver', 'Liver'),
    ('SCLC', 'SCLC'),
    ('Lymphoma', 'Lymphoma')]

CONSENT_CHOICES = [('Yes', 'Yes'), 
    ('No', 'No')]

STATUS_CHOICES = [('Banking', 'Banking'),
    ('Terminated', 'Terminated'),
    ('Frozen', 'Frozen'),
    ('Rebanked', 'Rebanked'),
    ('Thawed and Rebanked', 'Thawed and Rebanked')
]

SUBTYPE_CHOICES = [('Tumor', 'Tumor'),
    ('Normal', 'Normal'),
    ('Stroma', 'Stroma')

]

MEDIA_CHOICES = [('GHM', 'GHM'),
('DMEM', 'DMEM'),
('CHK', 'CHK'),
('WRN', 'WRN'),
('1% FBS', '1% FBS'),
('SHM', 'SHM'),
('CHM', 'CHM'),
('10% FBS', '10% FBS')

]

# SAMPLE_CHOICES = samples.objects.values_list('sample_id', 'sample_name')

class culture_info_form(forms.ModelForm):
    # sample_name = forms.ChoiceField(
    #     required=False,
    #     widget=forms.Select,
    #     choices=SAMPLE_CHOICES,
    # )
    first_culture = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'Date'}))
    last_culture = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'Date'}))
    date_consent = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'Date'}), required=False)
    culture_status = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=STATUS_CHOICES,
    )
    subtype_info  = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=SUBTYPE_CHOICES,
    )

    patient_consent = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CONSENT_CHOICES,
    )
    #If choice is No, Remove DATE FIELD
    passage = forms.ChoiceField(choices=[(x, x) for x in range(0, 40)])
    defrozen_passage = forms.ChoiceField(choices=[(x, x) for x in range(0, 40)])

    media = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=MEDIA_CHOICES,
    )
    tumor_type = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=TUMOR_CHOICES,
    )
    status = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=STATUS_CHOICES,
    )

    class Meta:
        model = culture_info
        
        exclude = ['subtype_id']
        # exclude = ['subtype_id', 'sample_id']
        # = ['passage', 'subtype']

class samples_form(forms.ModelForm):
    
    organ = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=ORGAN_CHOICES,
    )

    tumor_type = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=TUMOR_CHOICES,
    )

    general_consent = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CONSENT_CHOICES,
    )

    class Meta:
        model = samples
        exclude = ['sample_id']

        # = ['passage', 'subtype']

class molecular_order_form(forms.ModelForm):

    class Meta:
        model = molecular_order
        exclude = []
        # = ['passage', 'subtype']

class passages_form(forms.ModelForm):

    class Meta:
        model = processing
        exclude = []
        # = ['passage', 'subtype']

class freezing_form(forms.ModelForm):

    class Meta:
        model = freezing
        exclude = []
        # = ['passage', 'subtype']
