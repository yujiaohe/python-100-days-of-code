import os
import stripe

stripe.api_key = os.getenv("API_KEY")


class StripeProduct:
    def __init__(self, name, price, img_url):
        self.name = name
        self.price = int(price * 100)
        self.images = [img_url]

    def register_new_stripe(self):
        product = stripe.Product.create(name=self.name,
                                        images=self.images
                                        )
        stripe.Price.create(product=product.get('id'),
                            unit_amount=self.price,
                            currency="eur"
                            )
        return product.get('id')
