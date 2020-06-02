from django import forms

class StudentRegistration(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email_add=forms.EmailField()

class FormFieldWithArguments(forms.Form):
    #name = forms.CharField(label='Your Name',label_suffix='  ')
    #name = forms.CharField(label='Your Name',label_suffix='  ',initial='Ajul')
    #name = forms.CharField(label='Your Name',initial='Ajul',required=False)

    name = forms.CharField(label='Your Name',help_text='limit should be 50 character')

    address = forms.CharField(label='Your Address',disabled=True)