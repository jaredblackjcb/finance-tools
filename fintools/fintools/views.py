from django.shortcuts import render, redirect
from calculator import forms
from calculator.models import MailingMember
from django.contrib import messages

# Create your views here.
def index(request):
    form = forms.MailingList()
    context = {'form': form}
    if request.method == 'POST':
        form = forms.MailingList(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            member, created = MailingMember.objects.get_or_create(name=name, email=email)
            if created:
                member.save()
                messages.success(request, "Thanks for signing up! We'll be in touch soon!")
            else:
                messages.error(request, "User already exists. Please enter a unique name and email address.")
            return redirect('index')
        else:
            messages.error(request, form.errors['email'])
    return render(request, 'index.html', context=context)
