from django import forms
from django. 
from django.contrib.auth.forms import UserCreationForm
from lokale.models import Client

class ClientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Client
        fields = ('nick','cont','email')

    def save(self, commit=True):
        user = super(ClientRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
