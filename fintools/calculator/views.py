from django.shortcuts import render
from django import views
from django.views import View
from . import forms

# Create your views here.
def pmi_calculator(request):
    context_dict = {}
    return render(request, 'calculator/pmi_calculator.html', context=context_dict)

def annuity_calculator(request):
    annuity_calculator_form = forms.AnnuityCalculator(request.POST)
    future_value = 0
    context_dict = {'future_value': future_value, 'annuity_calculator_form': annuity_calculator_form}
    if request.method == 'POST':
        if annuity_calculator_form.is_valid():
            payment = annuity_calculator_form.cleaned_data['payment']
            interest_rate = annuity_calculator_form.cleaned_data['interest_rate']
            periods = annuity_calculator_form.cleaned_data['periods']
            future_value = (payment * ((1 + interest_rate) ** periods - 1) / interest_rate)
            context_dict['future_value'] = future_value
            print(payment)
            print(interest_rate)
            print(periods)
            print(future_value)
            print(context_dict)
    return render(request, 'calculator/annuity_calculator.html', context=context_dict)

