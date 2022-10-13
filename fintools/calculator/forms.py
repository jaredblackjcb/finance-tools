from django import forms
from . import models
class AnnuityCalculator(forms.Form):
    payment = forms.FloatField(label="Payment", help_text="Payment is the amount of money received from an annuity in a given period")
    interest_rate = forms.FloatField(label="Interest Rate", help_text="Interest Rate per period")
    periods = forms.IntegerField(label="Periods", help_text='Number of periods')

class MailingList(forms.ModelForm):
    class Meta:
        model = models.MailingMember
        fields = ['name', 'email']