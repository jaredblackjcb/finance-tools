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

class PmiCalculator(forms.Form):
    purchase_price = forms.FloatField(label="Purchase Price")
    down_payment = forms.FloatField(label="Down Payment %")
    interest_rate = forms.FloatField(label="Interest Rate %")
    loan_term = forms.IntegerField(label="Loan Term (Years)")
    monthly_pmi_payment = forms.FloatField(label="Monthly PMI Payment")
    opportunity_cost_roi = forms.FloatField(label="Market Return %", help_text="What rate of return would you get if you invested the money that is currently going toward mortgage insurance?")