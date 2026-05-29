# import sys

# for i, path in enumerate(sys.path):
#     print(f"{i}: {path}")

def get_tax(price, tax_rate=0):
    return price * tax_rate

def get_price(price, tax_rate, discount=0):
    disc_price = price * (1 - discount)
    net_price = disc_price * (1 + tax_rate)
    return net_price

