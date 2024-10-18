from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description']

        # Optional: You can customize widgets if needed
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter asset name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter asset description', 'rows': 4}),
        }

        # Optional: You can add labels and help texts if needed
        labels = {
            'name': 'Asset Name',
            'description': 'Asset Description',
        }

        help_texts = {
            'name': 'Please provide a unique name for the asset.',
            'description': 'Provide a detailed description of the asset.',
        }

