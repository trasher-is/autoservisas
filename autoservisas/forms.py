from django import forms
from django.contrib.auth.models import User
from .models import UzsakymasReview, Profilis, Uzsakymas, UzsakymoEilute

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


class DateInput(forms.DateInput):
    input_type = 'date'


class UzsakymasCreateForm(forms.ModelForm):
    class Meta:
        model = Uzsakymas
        fields = ['vartotojas', 'automobilis_id', 'grazinimo_terminas']
        widgets = {'vartotojas': forms.HiddenInput(), 'grazinimo_terminas': DateInput()}


class UzsakymoEiluteForm(forms.ModelForm):
    class Meta:
        model = UzsakymoEilute
        fields = ['paslauga_id', 'kiekis', 'uzsakymas_id']
        widgets = {'uzsakymas_id': forms.HiddenInput()}