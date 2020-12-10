from django import forms

SELECT_CHOICES = [
    ('1', 'one'),
    ('2', 'two'),
    ('3', 'three'),
    ('4', 'four'),
    ('5', 'five')
]

class ReviewForm(forms.Form):
    rate = forms.ChoiceField(label="Rating",
        widget=forms.RadioSelect(), choices=SELECT_CHOICES)
    comment = forms.CharField(label="Comment",
        widget=forms.Textarea(attrs={
            'class': 'form-control md-textarea',
            'rows': 3
        }))