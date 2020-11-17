from django import forms


class AddItemToCartForm(forms.Form):
    quantity = forms.CharField(max_length=20)