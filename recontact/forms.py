from django.forms import Form, CharField, EmailField, Textarea, TextInput, EmailInput
from django.core.exceptions import ValidationError

import re

has_url = re.compile("https?://") 

def no_click_bait(value):
    if has_url.search(value):
        raise ValidationError('Please remove all URLs.')

class RecontactForm(Form):
    """
    Django form which collects data for a contact email message.
    """
    sender = CharField(label='', widget=TextInput(
        attrs={'placeholder': 'Your Name', 'class': 'recontact'}),
        validators=[no_click_bait])
    
    reply_to = EmailField(label='', widget=EmailInput(
        attrs={'placeholder': 'Your email address', 'class': 'recontact'}))

    subject = CharField(label='', widget=TextInput(
        attrs={'placeholder': 'Subject', 'class': 'recontact'}),
        validators=[no_click_bait])

    message = CharField(label='', widget=Textarea(
        attrs={'placeholder': 'Message', 'class': 'recontact'}),
        validators=[no_click_bait])
