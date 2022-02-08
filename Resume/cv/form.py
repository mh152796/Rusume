from dataclasses import field
from django.forms import ModelForm
from . models import ResumeModel

class Form(ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['name', 'phone', 'address', 'objective', 'work_experience','edu_qualification',
                  'social_facebook', 'social_instagram', 'social_linkedin', 'image',
                  ]
        
        
        
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Your Phone Number'
        self.fields['address'].widget.attrs['placeholder'] = 'Address....'
        self.fields['objective'].widget.attrs['placeholder'] = 'Objective....'
        self.fields['work_experience'].widget.attrs['placeholder'] = 'Work Experience....'
        self.fields['edu_qualification'].widget.attrs['placeholder'] = 'Educational Qualification'
        self.fields['social_facebook'].widget.attrs['placeholder'] = 'Facebook....'
        self.fields['social_instagram'].widget.attrs['placeholder'] = 'Instragram....'
        self.fields['social_linkedin'].widget.attrs['placeholder'] = 'Linkedin....'
        self.fields['address'].widget.attrs['rows'] = '3'
        self.fields['edu_qualification'].widget.attrs['rows'] = '5'
        self.fields['work_experience'].widget.attrs['rows'] = '6'
        self.fields['objective'].widget.attrs['rows'] = '6'
        
        for name, field in self.fields.items():
             field.widget.attrs.update({'class':'form-control'}) 