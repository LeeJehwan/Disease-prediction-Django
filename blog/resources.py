from import_export import resources
from .models import Person
from .models import Train_data


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class TrainResource(resources.ModelResource):
    class Meta:
        model = Train_data