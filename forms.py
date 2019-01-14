from django import forms                                                           
from .models import ImageFiles

class ImgForm(forms.ModelForm):

    class Meta:
        model = ImageFiles
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
           
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
}
