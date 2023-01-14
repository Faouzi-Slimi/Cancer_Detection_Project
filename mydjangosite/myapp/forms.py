from django import forms
from django import forms
from .models import Document

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


from django import forms


class GeeksForm(forms.Form):
    name = forms.CharField()
    geeks_field = forms.ImageField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


from django import forms
from .models import *


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
from django import forms
from .models import Image

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
