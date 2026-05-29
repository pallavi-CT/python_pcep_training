# import modules_ex as pricing

# # from modules_ex import get_price, get_tax

# final_price = pricing.get_price( price=1000, tax_rate=0.01
# )

# print(final_price)



# ecommerce/
#   | - products/
        # | - crud operations (.py)
#   | - customers/
#           | - crud 
#               - validations etc


from validators import validate_email

def register_user(email:str, name: str) -> dict:
    ok, error = validate_email(email)

    if not ok:
        return {'success': False, 'error': error}
    
    return {'success': True, 'email': email, 'name': name}


print(register_user('alice@example.com', 'Alice Smith'))

print(register_user('beth@tempmail.com', 'Beth Jones'))



