from django import forms
from .models import Category
from .models import Perizinan
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =('name','note',)

class PermissionForm(forms.ModelForm):
    class Meta:
        model = Perizinan
        fields =('employee','start','end','category','reason',)
