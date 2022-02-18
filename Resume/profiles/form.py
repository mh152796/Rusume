import imp
from tkinter import Widget
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, TextInput, fields
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        # def __init__(self, *args, **kwargs):
        # super(Form, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Name'
        # self.fields['phone'].widget.attrs['placeholder'] = 'Enter Your Phone Number'
        # self.fields['address'].widget.attrs['placeholder'] = 'Address....'
        # self.fields['objective'].widget.attrs['placeholder'] = 'Objective....'
        
        # widgets = {
        #     'password1': TextInput(attrs={'placeholder':'000000'}),
        #     'password2': TextInput(attrs={'placeholder':'000000'}),
        # }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial='username'
        self.fields['email'].widget.attrs['placeholder'] = 'email address....'
        self.fields['password1'].widget.attrs['placeholder'] = '******'
        self.fields['password2'].widget.attrs['placeholder'] = '******'
        for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'}) 
                
    # def clean_name(self):
    #     username1=self.cleaned_data.get('username')
    #     value1=len(username1)
        
    #     if value1>10:
    #         self.add_error('username', 'you password must be have 8 charecter or more')
    #     else:
    #         return username1  
     
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'phone', 'email',
                  'short_intro','location','social_facebook','social_instagram','social_linkedin','address', 'image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['rows'] = '3'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            