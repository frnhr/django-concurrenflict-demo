from django.contrib import admin
from concurrenflict.forms import ModelForm
from .models import MyTag, MyModel


class MyTagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(MyTag, MyTagAdmin)


class MyModelAdminForm(ModelForm):
    pass

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field_a', 'field_b', 'field_d', )
    form = MyModelAdminForm

admin.site.register(MyModel, MyModelAdmin)
