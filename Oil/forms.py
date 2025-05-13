from django import forms
from .models import ContactMessage, OilProduct

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class OilProductForm(forms.ModelForm):
    class Meta:
        model = OilProduct
        fields = '__all__'
