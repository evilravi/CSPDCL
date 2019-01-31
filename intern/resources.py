from import_export import resources
from .models import Courses, Batch, Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
