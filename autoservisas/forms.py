from django import forms
from django.contrib.auth.models import User
from .models import UzsakymasReview, Profilis

class UzsakymasReviewForm(forms.ModelForm):
    class Meta:
        model = UzsakymasReview
        fields = ('atsiliepimo_tekstas', 'uzsakymas_review_id', 'reviewer',)
        widgets = {'uzsakymas_review_id': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']