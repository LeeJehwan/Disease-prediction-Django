from django.contrib import admin
from .models import Post
from .models import Train_data
from .models import Person1_train
from import_export.admin import ImportExportModelAdmin
from .models import Person

admin.site.register(Post)
admin.site.register(Person1_train)
# @admin.register(Person)

#class PersonAdmin(ImportExportModelAdmin):
#    pass

#admin.site.register(Train_data)


@admin.register(Train_data)
class TrainAdmin(ImportExportModelAdmin):
    pass




