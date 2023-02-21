from django import forms


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

    

    