import string
import random

# 1. Shopping cart simulator
def test_calculate_cart_total(dic, iva= 0.21):
    subT = 0
    for i in dic:
        priceP = i['price']
        qnt = i['quantity']
        subT += priceP * qnt
    total = subT *(1 + iva)
    return round(total,2)

cart = [
        {"name": "Shirt", "price": 20.0, "quantity": 2},
        {"name": "Pants", "price": 40.0, "quantity": 1}
    ]
print(test_calculate_cart_total(cart,0.21))

# 2. Text processing (word count)

    

# 3. Secure password generator


# 4. Weather analyzer (temperatures)


# 5. Functional contact book
