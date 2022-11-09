from django import forms

class BactesterForm(forms.Form):
    ticker = forms.CharField(max_length=10)
    start_date = forms.DateField()
    end_date = forms.DateField()
    monthly_investment = forms.FloatField()