from foodstore import models


class Cart:
    def __init__(self, cart_data={}, total_price=0):
        self.cart_data = cart_data
        self.total_price = total_price
        self.length = len(cart_data)

    
    def add_item_to_cart(self, item_id, amount):
        if item_id in self.cart_data.keys():
            self.cart_data[item_id]['amount'] += amount
            self.cart_data[item_id]['total_price'] += self.cart_data[item_id]['price'] * amount
            self.total_price += self.cart_data[item_id]['price'] * amount
        else:
            product = models.Product.objects.get(pk=item_id)
            self.cart_data[item_id] = {
                    'amount': amount,
                    'price': product.price,
                    'total_price': product.price * amount
                }
            self.total_price += product.price * amount
            self.length += 1

    def edit_cart_data(self, new_data):
        self.cart_data = new_data

    
    def get_serialized_data(self):
        return {
            'cart_data': self.cart_data,
            'total_price': self.total_price,
            'length': self.length,
        }


def get_cart_from_session(request):
    # Check cart from session
    try:
        current_data = request.session['cart']
    except KeyError:
        current_data = None

    if current_data:
        # If existed, create cart object from session data
        return Cart(cart_data=current_data['cart_data'], 
                total_price=current_data['total_price'])
    else: 
        # If not, create a new empty cart object 
        return Cart()