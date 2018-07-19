from django import forms
from .models import Category
from .models import Perizinan

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =('name','note',)

class PermissionForm(forms.Form):
    class Meta:
        model = Perizinan
        fields =('employee','start','end','category','reason',)
