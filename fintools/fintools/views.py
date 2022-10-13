from django.shortcuts import render
from calculator import forms

# Create your views here.
def index(request):
    form = forms.MailingList(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
    return render(request, 'index.html', context={'form': form})
