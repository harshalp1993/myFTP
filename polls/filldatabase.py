from polls.models import Samples
import string

Samples.objects.create(
    SampleID = '123450',
    SampleName = 'SKM4',
    CancerType = 'Sarcoma',
)

#Retrieving records
samples_list = Samples.objects.all()

#For deleting 
#Samples.objects.filter(SampleName = 'SKM3').delete()


#Import data to Cultures
from polls.models import CultureInfo


culture = CultureInfo(
    SubtypeID = '234567',
    SampleID == '123450',
    SubtypeInfo = 'Sarcomadefault',
    FirstCulture = '2020-12-10',
    Passage = '2',
    Media = 'DMSO',
    CultureType = 'Par',
    CellBlock = 'Example',
    KnownMutation = '',
    MolecularOrder = '',
    PatientConsent = '',
    DateOfConsent = '2020-12-10',
    Comments = '',


)

from polls.models import CultureInfo, Samples, Processing

a = Samples(
    SampleID = '123459',
    SampleName = 'SKM9',
    CancerType = 'Sarcoma',
)

a.save()

b = CultureInfo(
    SampleID = a,
    SubtypeID = '234569',
    SubtypeInfo = 'Sarcomadefault',
    FirstCulture = '2020-12-15',
    Passage = '2',
    Media = 'DMSO',
    CultureType = 'Par',
    CellBlock = 'Example',
    KnownMutation = 'YES',
    MolecularOrder = '',
    PatientConsent = '',
    DateOfConsent = '2020-12-16',
    Comments = '',


)
b.save()

c = Processing(
    ProcessingID = '123459',
    SubtypeID = b,
    Subcategory = 'Sarcomadefault',
    PassageDate= '2020-12-10',
    Media = 'DMSO',
    PassageNumber = '3',
    CultureType = 'Normal',
    Comments = '',
)
c.save()


from polls.models import MolecularOrder

d = MolecularOrder(
    MolecularOrderID     = '1234567',
    SubtypeID            = b,
    MolecularOrderNumber = '0000',
    AssayType =''
)

d.save()


from polls.models import Freezing


e = Freezing(
    FreezingID   = '12345',
    ProcessingID = c,
    Amount       = 2,
    FreezingType = 'None',
    Location     = '23.Lab1',
    Tower        = '1',
    Box          = '234',
    Start        = '2020-12-16',
    End          = '2020-12-16',
    Comments     = '',
    FrozenBy     = 'Person1',

)
e.save()


#Introduce data into database:
import pandas as pd
df = pd.read_csv('/home/USZ/plialacc/Pliego-Alicia/TablesDB/Samplescurated2.tsv', sep = '\t', header=None)
for index,row in df.iterrows():
    samples.objects.create(sample_id = row[0],
    sample_name = row[1],
    organ = row[7],
    tumor_type = row[2],
    additional = row[3],
    molecular_general = row[4],
    molecular_organoid= row[5],
    general_consent=row[6] )

#Import cultures
import pandas as pd
df = pd.read_csv('/home/USZ/plialacc/Pliego-Alicia/TablesDB/culture_info.tsv', sep = '\t', header=None)
for index,row in df.iterrows():
    culture_info.objects.create(subtype_id = row[0],
    sample_id_id = row[1],
    subtype_info = row[2],
    first_culture   = row[3], 
    culture_status  = row[4],
    passage = row[5],
    defrozen_passage = row[6],
    media   = row[7],
    tumor_type = row[8],
    culture_type = row[9],
    status = row[10],
    last_culture = row[11],
    cell_block = row[14],
    known_mutation = row[15],
    molecular_order_number = row[16],
    patient_consent = row[17],
    date_consent = row[18],
    note = row[12],
    note_2 = row[13])


    
       