from django import forms


class ReviewForm(forms.Form):
    rate = forms.IntegerField(label="Rating",
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    comment = forms.CharField(label="Comment",
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        }))