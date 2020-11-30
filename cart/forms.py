from django import forms
from cart.models import Order


class OrderForm(forms.Form):
    first_name = forms.CharField(label='First Name', 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    last_name = forms.CharField(label='Last Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    detail_address = forms.CharField(label='Address', 
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Appartement, building, ect...'
        }))
    street = forms.CharField(label="Street", 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    city = forms.CharField(label="City",
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    phone = forms.CharField(label="Phone Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    email = forms.EmailField(label="Email", 
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }))
    addition_note = forms.CharField(label="Notes", 
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your remark to us...'
        }), 
        required=False)




class AddItemToCartForm(forms.Form):
    quantity = forms.FloatField(initial=0, 
        widget=forms.TextInput())


class CartEditForm(forms.Form):
    """
    Form used to edit cart before checkout
    Extra fields in kwargs will be cartitem for each carted product
    Total price field managed by js
    """
    # Used to fetch to form
    total_price = forms.FloatField(initial=0, 
        widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        """
        The form inited with 'extra' keyword in case of GET form
        as its rendering based on session's cart items number
        In other methods, 'extra' won't be passed in
        """
        try:
            extra = kwargs.pop('extra')
        except KeyError:
            extra = None
        super().__init__(*args, **kwargs)

        if extra:
            for item in extra:
                if item != 'total_price':
                    self.fields[item] = forms.IntegerField(
                        widget=forms.TextInput(), initial=extra[item])


    def get_field(self, field_name):
        return self.fields[field_name]