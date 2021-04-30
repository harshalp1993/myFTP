#root /path/to/models.py
#models package from Django.db

import django 
from django.db import models 

class samples(models.Model):
    ''' Insert the Samples which come directly from the tissue '''
    sample_id            = models.IntegerField(primary_key = True)
    sample_name          = models.CharField(max_length = 50, null = True, blank = True)
    organ                = models.CharField(max_length = 40, null = True, blank = True)
    tumor_type           = models.CharField(max_length = 50, null = True, blank = True)
    additional           = models.CharField(max_length = 40, null= True, blank = True)
    molecular_general    = models.CharField(max_length = 40, null=True, blank = True)
    molecular_organoid   = models.CharField(max_length = 40, null = True, blank = True)
    general_consent      = models.CharField(max_length = 40, null = True, blank = True)
    def __str__(self):
        return str(self.sample_id)
    def save(self, *args, **kwargs):
        if not self.sample_id:
            count = samples.objects.count()
            self.sample_id = format(count+1)
        super().save(*args, **kwargs)
    

class tissue(models.Model):
    tissue_id = models.CharField('Tissue_id', primary_key = True, max_length = 20)
    sample_id = models.ForeignKey(samples, on_delete = models.CASCADE)
    def __str__(self):
        return self.tissue_id

class patient_info(models.Model):
    patient_id = models.CharField(primary_key = True, max_length = 20)
    tissue_id  = models.ForeignKey(tissue, max_length = 20, on_delete = models.CASCADE)
    name       = models.CharField(max_length = 30, null=True, blank = True)
    surname    = models.CharField(max_length = 40, null= True)
    gender     = models.CharField(max_length = 20, null=True)

class biobank(models.Model):
    biobankID = models.CharField(primary_key = True, max_length = 20)
    tissueID  = models.ForeignKey(tissue, max_length = 20, on_delete = models.CASCADE)
    def __str__(self):
        return self.biobank_id
        
class culture_info(models.Model):
    subtype_id        = models.CharField(primary_key = True, max_length=20)
    sample_id         = models.ForeignKey(samples, on_delete=models.CASCADE)
    sample_name       = models.CharField('sample_id', max_length=50, blank=True, null=True)
    subtype_info      = models.CharField(max_length = 30, null = True)
    first_culture     = models.DateField('First Passage',blank = True, null = True)
    culture_status    = models.CharField(max_length = 40, null = True, blank = True)
    passage           = models.CharField(max_length = 30, null = True, blank = True)
    defrozen_passage  = models.CharField(max_length = 40, null = True, blank = True)
    media             = models.CharField(max_length = 30, null = True, blank=True)
    tumor_type        = models.CharField(max_length = 30, null = True, blank=True)
    culture_type      = models.CharField(max_length = 40, null = True, blank = True)
    status            = models.CharField(max_length = 40, null = True, blank = True)
    last_culture      = models.DateField('Last Passage',blank = True, null = True)
    cell_block        = models.CharField(max_length = 30, null= True, blank=True)
    known_mutation    = models.CharField(max_length = 30, null= True, blank=True)
    molecular_order_number   = models.CharField(max_length = 10, null= True, blank=True)
    patient_consent   = models.CharField(max_length = 30, null = True, blank=True)
    date_consent      = models.DateField('Date of Consent', null = True, blank=True)
    note              = models.CharField(max_length = 120, null = True, blank = True)
    note_2            = models.CharField(max_length = 120, null = True, blank = True)
    
    def __str__(self):
        return str(self.subtype_id)

    def save(self, *args, **kwargs):
        if not self.subtype_id:
            self.sample_id = samples.objects.filter(sample_name=self.sample_name).values()[0]['sample_id']
            count = culture_info.objects.filter(sample_id=self.sample_id).count()
            self.subtype_id = "{}.{}".format(self.sample_id, count+1)
            # count = culture_info.objects.count()
            # self.subtype_id = "{}".format(count+1)
        super().save(*args, **kwargs)


class mutations(models.Model):
    mutation_id         = models.CharField(primary_key = True, max_length = 20)
    subtype_id          = models.ForeignKey(culture_info, on_delete = models.CASCADE)
    gene_name           = models.CharField(max_length = 30, null = True)
    chromosome          = models.CharField(max_length = 10, null = True)
    chromosome_position = models.IntegerField(null = True)
    gene_position       = models.IntegerField(null = True)
    protein_position    = models.IntegerField(null = True)

class molecular_order(models.Model):
    molecular_order_id     = models.CharField(primary_key = True, max_length = 20)
    subtype_id             = models.ForeignKey(culture_info, on_delete = models.CASCADE)
    molecular_order_number = models.CharField(max_length = 30, null = True)
    assay_type             = models.CharField(max_length = 30, null = True)

class processing(models.Model):
    processing_id       = models.CharField(primary_key = True, max_length = 20)
    subtype_id          = models.ForeignKey(culture_info, max_length = 20, on_delete = models.CASCADE)
    tumor_type          = models.CharField(max_length = 50, null = True, blank = True)
    passage_date        = models.DateTimeField(null = True, blank = True)
    media               = models.CharField(max_length = 40, null = True, blank = True)
    passage_number      = models.IntegerField(null = True, blank = True)
    defrozen_passage    = models.IntegerField(null = True, blank = True)
    status_passage      = models.CharField(max_length = 50, null = True, blank = True)
    format_processing   = models.CharField(max_length = 50, null = True, blank = True)
    culture_type        = models.CharField(max_length = 40, null = True)
    format_number       = models.CharField(max_length = 40, null = True)
    cell_block          = models.CharField(max_length = 40, null = True)
    smear               = models.CharField(max_length = 40, null = True)
    date_block          = models.DateTimeField( null = True, blank = True)
    comments            = models.TextField(blank = True, null = True)



class freezing(models.Model):
    freezing_id         = models.CharField(primary_key = True, max_length = 25)
    type_freezing       = models.CharField(max_length = 40, null = True)
    sample_id           = models.ForeignKey(samples, on_delete = models.CASCADE)
    defrozen_passage    = models.IntegerField(null = True, blank = True)
    date                = models.DateTimeField( null = True)
    passage_number      = models.IntegerField(null = True, blank = True)
    amount              = models.IntegerField(null = True, blank = True)
    freezing_type       = models.CharField(max_length = 40, null = True, blank = True)
    location            = models.CharField(max_length = 40, null = True)
    tower               = models.CharField(max_length = 30, null = True)
    box                 = models.CharField(max_length = 40, null = True)
    start               = models.CharField(max_length = 40, null = True)
    end                 = models.CharField(max_length = 40, null = True)
    frozen_by           = models.CharField(max_length = 40, null = True)
    vials_removed       = models.CharField(max_length = 40, null = True)
    date_removed        = models.DateTimeField( null = True)
    box_removed         = models.CharField(max_length = 40, null = True)
    start_removed       = models.CharField(max_length = 40, null = True)
    end_removed         = models.CharField(max_length = 40, null = True)
    removed_by          = models.CharField(max_length = 40, null = True)
    sent_to             = models.CharField(max_length = 40, null = True)



