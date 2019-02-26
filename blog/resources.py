from import_export import resources
from .models import Person
from .models import Train_data
from .models import Person1_train


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class TrainResource(resources.ModelResource):
    class Meta:
        model = Train_data


class Person1Resouece(resources.ModelResource):
    class Meta:
        model = Person1_train
