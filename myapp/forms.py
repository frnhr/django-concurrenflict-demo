from .models import MyModel
from concurrenflict.forms import ModelForm


class MyModelForm(ModelForm):

    class Meta:
        model = MyModel
