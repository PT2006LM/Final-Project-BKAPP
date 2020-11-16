from foodstore import models


class Cart:
    def __init__(self, cart_data={}, total_price=0):
        self.cart_data = cart_data
        self.total_price = total_price

    
    def add_item_to_cart(self, item_id, amount):
        if item_id in self.cart_data.keys():
            self.cart_data[item_id]['amount'] += amount
            self.cart_data[item_id]['total_price'] += self.cart_data[item_id]['price'] * amount
        else:
            product = models.Product.objects.get(pk=item_id)
            self.cart_data[item_id] = {
                item_id: {
                    'amount': amount,
                    'price': product.price,
                    'total_price': product.price * amount
                }
            }

    def edit_cart_data(self, new_data):
        self.cart_data = new_data