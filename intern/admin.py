from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Courses, Batch, Person , Image, Contact
from .resources import PersonResource


admin.site.register(Courses)

admin.site.register(Batch)

admin.site.register(Contact)
admin.site.register(Image)
@admin.register(Person)

class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = (
                    ('Course', admin.RelatedOnlyFieldListFilter,  ),
                    ('Batch_No', admin.RelatedOnlyFieldListFilter, ),

    )
    pass
