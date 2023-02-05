from django import forms
from musker.models import Meep


class MeepForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter your meep"}
        ),
        label="",
    )

    class Meta:
        model = Meep
        exclude = ("user",)
