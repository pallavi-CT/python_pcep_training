# def greet(name: str, greeting: str ='Hello') -> str:
#     # return greeting + ' ' + name
#     return f"{greeting}, {name.capitalize()}"

# print(greet('Pallavi'))

# def min_max(numbers: list) -> tuple:
#     return min(numbers), max(numbers)

# least, highest = min_max([5, 7, 1, 8, 2])
# print(least)
# print(highest)

# def make_multiplier(factor):
#     def multiply(x):
#         return x * factor
#     return multiply

# double = make_multiplier(2)
# val = double(5)
# print(val)

# *args, **kwargs
# def add(*values):
#     print(f"Total: {sum(values)}")

# add(1, 2)
# add(2, 4, 5, 6)

# def build_user_profile(user_id, **attributes):
#     profile = {'id': user_id}
#     profile.update(attributes)
#     return profile

# user_profile = build_user_profile("U001", name="Prasad", dept="IT", salary="56700", remote=False)
# print(user_profile)

# square = lambda x: x**2
# add = lambda a, b: a + b

# print(square(3))
# print(add(3, 5))

# def transform_vals(data: list, transform_fn):
#     # squares = []
#     # for item in data:
#     #     x = item ** 2
#     #     squares.append(x)
    
#     # return squares
#     return [transform_fn(item) for item in data]

# print(transform_vals([2, 4, 6], lambda x: x**2))

def log_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling: {fn.__name__}")
        result = fn(*args, **kwargs)
        print(f"Done: returned {result}")
        return result
    return wrapper

@log_call
def build_user_profile(user_id, **attributes):
    profile = {'id': user_id}
    profile.update(attributes)
    return profile

build_user_profile("U001", name="Prasad", dept="IT", salary="56700", remote=False)

@log_call
def add(a, b):
    return a + b

add(3, 5)