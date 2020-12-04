from django import forms
from core2.tasks import send_review_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Firstname', max_length=60, widget=forms.TextInput(attrs= {
            'class': 'form-control mb-3', 
            'placeholer': 'First Name',
            'id': 'form-firstname'
        })
    )

    email = forms.EmailField(
        label='Email', max_length=60, widget=forms.TextInput(attrs= {
            'class': 'form-control mb-3', 
            'placeholer': 'Email',
            'id': 'form-email'
        })
    )

    review = forms.CharField(

        label='Review', widget=forms.TextInput(attrs= {
            'class': 'form-control', 
            'rows': '5',
          
        })
    )

    def send_email(self):
        send_review_email_task.delay(
        self.cleaned_data.get('name'), self.cleaned_data.get('email'), self.cleaned_data.get('review')
        )