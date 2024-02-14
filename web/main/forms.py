from django import forms
from .models import User

class loginForm(forms.Form):
    login = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'You\'re name here...'}))
    
    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data['login']
        
        if not login:
            self.add_error('login', 'You skipped field!')
            return cleaned_data
        
class SendValentineForm(forms.Form):
    recipient = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'You\'re Valentine here...'}))
    message = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'placeholder': 'You\'re question here...'}))
    
class SendAnswerForm(forms.Form):
    answer = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'You\'re answer here...'}))