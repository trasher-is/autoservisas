from .models import UzsakymasReview
from django import forms

class UzsakymasReviewForm(forms.ModelForm):
    class Meta:
        model = UzsakymasReview
        fields = ('atsiliepimo_tekstas', 'uzsakymas_review_id', 'reviewer',)
        widgets = {'uzsakymas_review_id': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}