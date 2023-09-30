from django import forms
from .models import Classes,Section

class ClassForm(forms.ModelForm):
    class Meta:
        model= Classes
        fields=['class_name']

class SectionForm(forms.ModelForm):
    class Meta:
        model= Section
        fields=['class_name','section_name']

class SectionSearch(forms.Form):
    class_name=forms.CharField(max_length=100, label='Enter Class to Search')



                                 

