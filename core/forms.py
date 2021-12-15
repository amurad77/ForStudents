from django import forms

from core.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'number',
            'email',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    # 'id': 'remove_input',
                                    'class': 'app-form-control',
                                    'placeholder':"Adınız",
                                }),
            'number': forms.TextInput(attrs={
                                    'type' : 'number',
                                    # 'id': 'remove_input',
                                    'class': 'app-form-control',
                                    'placeholder':"Nömrəniz",
                                }),
            'email': forms.EmailInput(attrs={
                                    # 'id': 'remove_input',
                                    'class': 'app-form-control',
                                    'placeholder':"E-mail",
                                }),
            'message': forms.TextInput(attrs={
                                    # 'id': 'remove_input',
                                    'class': 'app-form-control',
                                    'placeholder':"Mesajınız",
                                }),
        }

