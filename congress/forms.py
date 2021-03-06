from django import forms


class VotingForm(forms.Form):
    OPTIONS = (
        ("y", "За"),
        ("n", "Против"),
        ("a", "Воздержался"),
    )
    vote_choice = forms.ChoiceField(choices=OPTIONS, required=True)

    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}), required=False)


class MessageForm(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}), required=True)
    photo = forms.ImageField()