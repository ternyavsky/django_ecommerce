from django import forms
from django.forms import ModelForm
from .models import UserAddress

class SendForm(forms.Form):
    
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'subject',
        'placeholder':'Your subject of this message',
        'type':'text'
    }))

    message = forms.CharField(max_length=220,widget=forms.Textarea(attrs={
        'class':'form-control',
        'id':'message',
        'placeholder':'Say something about us',
        'type':'text',
        'name':'message',
        'cols':'30',
        'rows':'10'
    }))



class AddressForm(ModelForm):
    address = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "placeholder":"Address...",
        "name":"address"

        }))
    city = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "placeholder":"City...",
        "name":"city"

        }))
    state = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"text",
        "placeholder":"State...",
        "name":"state"

        }))
    zipcode = forms.IntegerField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Zip code...",
        "name":"zipcode"

        }))
    
    class Meta:
        model = UserAddress
        fields = ['address','city','state','zipcode']


    

    