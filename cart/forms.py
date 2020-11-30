from django import forms
from cart.models import Order


class OrderForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    detail_address = forms.CharField(label='Address', 
        widget=forms.Textarea())
    street = forms.CharField(label="Street")
    city = forms.CharField(label="City")
    phone = forms.CharField(label="Phone Number")
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    addition_note = forms.CharField(label="Notes", 
        widget=forms.Textarea(), required=False)




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