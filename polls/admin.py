from django.contrib import admin
from .models import *

admin.site.register(samples)
admin.site.register(tissue)
admin.site.register(patient_info)
admin.site.register(biobank)
admin.site.register(culture_info)
admin.site.register(mutations)
admin.site.register(molecular_order)
admin.site.register(processing)
admin.site.register(freezing)

