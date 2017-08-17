from django.forms import Form, CharField, EmailField, Textarea, TextInput, EmailInput

class RecontactForm(Form):
    sender = CharField(label='', widget=TextInput(
        attrs={'placeholder': 'Your Name',
               'class': 'big'}))
    reply_to=EmailField(label='', widget=EmailInput(
        attrs={'placeholder': 'Your email address',
               'class': 'big'}))
    subject = CharField(label='', widget=TextInput(
        attrs={'placeholder': 'Subject',
               'class': 'big'}))
    message = CharField(label='', widget=Textarea(
        attrs={'placeholder': 'Message',
               'class': 'big'}))
