from django import forms


class AddItemToCartForm(forms.Form):
    quantity = forms.FloatField(initial=0, 
        widget=forms.TextInput())



class CartEditForm(forms.Form):
    # Form used to edit cart before checkout
    # Extra fields in kwargs will be cartitem for each carted product
    # Total price field managed by js
    total_price = forms.FloatField(initial=0, 
        widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        # The form inited with 'extra' keyword in case of GET form
        # as its rendering based on session's cart items number
        # In other methods, 'extra' won't be passed in
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