from django import forms

from myapp.models import singleImage


class singleImgForm(forms.ModelForm):
    class Meta:
        model = singleImage
        fields = "__all__"
        widgets = {
            'imgname': forms.TextInput(attrs={'class': 'form-control'}),
            'myImg': forms.FileInput(attrs={'class': 'form-control'}),
        }