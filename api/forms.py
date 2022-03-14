from django import forms

from .models import Doctor, Comment


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['image', 'title', 'category', 'degree', 'location', 'contact', 'appointment', 'fees']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment': forms.TextInput(attrs={'class': 'form-control'}),
            'fees': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Enter Doctor Name:',
            'image': 'Select an Image: ',
            'category': 'Select Category: ',
            'degree': 'Enter degree: ',
            'location': 'Enter location: ',
            'contact': 'Enter contact: ',
            'appointment': 'Enter appointment Process: ',
            'fees': 'Enter Doctor Fees: ',

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }
