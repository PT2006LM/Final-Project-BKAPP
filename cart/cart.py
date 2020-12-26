from foodstore.models import Product


class Cart:
    """
    Abstract object to deal with Product models from foodstore.
    cart_data store item as {
        'product_id': {
            'amount': ...,
            'price': ...,
            'total_price': ...
        }
    }
    """
    def __init__(self, cart_data={}, total_price=0):
        self.cart_data = cart_data
        self.total_price = total_price
        self.length = len(cart_data)

    
    def add_item_to_cart(self, item_id, amount):
        """
        Add item to the cart by product_id and amount.
        Cart item associated with product_id is validated and its price, amount
        are updated accordingly. 
        NOTE: Total price of cart also updated
        """
        item_id = str(item_id)
        if item_id in self.cart_data.keys():
            self.cart_data[item_id]['amount'] += amount
            self.cart_data[item_id]['total_price'] += self.cart_data[item_id]['price'] * amount
            self.total_price += self.cart_data[item_id]['price'] * amount
        else:
            product = Product.objects.get(pk=item_id)
            self.cart_data[item_id] = {
                    'amount': amount,
                    'price': product.price,
                    'total_price': product.price * amount
                }
            self.total_price += product.price * amount
            self.length += 1


    def update_cart_data(self, cart_data):
        """
        Reset data and re-fetched -- need to be further optimized

        Receive a raw dictionary of 'product_id': 'amount'
        'cart_data' refreshed and add each item in the dictionary to the cart
        """
        self.reset_data()
        for item in cart_data:
            self.add_item_to_cart(item, cart_data[item])
            if cart_data[item] == 0:
                del self.cart_data[item]

    
    def reset_data(self):
        self.cart_data = {}
        self.total_price = 0
        self.length = 0

    
    def get_serialized_data(self):
        """
        Get data needed to stored in session and can be deserialized
        to be processed in views
        """
        return {
            'cart_data': self.cart_data,
            'total_price': self.total_price,
            'length': self.length,
        }

    def is_empty(self):
        """
        Is this cart has any items
        """
        return self.cart_data == {}


def get_cart_from_session(request):
    """
    Deserialized cart data from session if existed or return an empty cart
    otherwise
    """
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
        return Cart({}, 0)