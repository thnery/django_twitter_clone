from django import forms

class TweetForm(forms.Form):
    text = forms.CharField(label='Tweet', max_length=200)
