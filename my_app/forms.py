from django import forms
from my_app.models import Weight

class WeightForm(forms.ModelForm):

    class Meta:
        model = Weight
        fields = ('weight',)
