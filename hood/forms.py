from django import forms
from .models import notifications,Business,Profile,BlogPost,Comment

class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']
