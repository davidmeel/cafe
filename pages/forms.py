from django import forms
from .models import ReservationModel

class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['name', 'email', 'message']

