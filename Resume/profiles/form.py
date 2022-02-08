import imp
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, fields
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            
        for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'}) 
                
                
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
            