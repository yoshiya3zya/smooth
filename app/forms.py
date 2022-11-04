from django import forms
from .models import PlacePhoto

class PlacePhotoForm(forms.ModelForm):
    class Meta:
        model = PlacePhoto
        fields = ['image',]

class PhotosForm(forms.Form):
    photos_field = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={'multiple': True}))
