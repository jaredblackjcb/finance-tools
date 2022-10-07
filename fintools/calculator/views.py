from django.shortcuts import render

# Create your views here.
def pmi_calculator(request):
    context_dict = {}
    return render(request, 'calculator/pmi_calculator.html', context=context_dict)