from django import forms
class AnnuityCalculator(forms.Form):
    payment = forms.DecimalField(label="Payment", max_digits=10, decimal_places=2, help_text="Payment is the amount of money received from an annuity in a given period")
    interest_rate = forms.DecimalField(label="Interest Rate", max_digits=5, decimal_places=2, help_text="Interest Rate per period")
    periods = forms.IntegerField(label="Periods", help_text='Number of periods')
