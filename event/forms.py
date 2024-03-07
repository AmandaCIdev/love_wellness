from .models import Reviews
from django import forms
class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('body',)