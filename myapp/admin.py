from django.contrib import admin
from .models import MyTag, MyModel


class MyTagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(MyTag, MyTagAdmin)


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field_a', 'field_b', 'field_d', )

admin.site.register(MyModel, MyModelAdmin)
