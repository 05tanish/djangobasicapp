from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):  # ✅ Correct PascalCase
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
