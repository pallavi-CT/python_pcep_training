# text = "Python Programming"

# print("Left to right")
# print(text[1])

# print("Right to left")
# print(text[-3])

# print(text[:5])

# print(text[::2])

# print(text[::-1])

# string methods:
# strip(), lower(), upper(), title(), replace, split, startsWith, endsWith, join, 
# find, count, isdigit

# customer = [
#     " john doe ",
#     "john@example.com",
#     " +91-20010222",
#     "1,23,345.88"
# ]

# name, email, phone, sal = customer

# clean_name = name.strip().title()
# clean_email = email.strip().lower()

# print("Name: ", clean_name)

# emp_id = "EMP-2024-AMR-00789"

#split
# emp_details = emp_id.split("-")

# year_of_joining = emp_details[1]
# location = emp_details[2]
# id = emp_details[3]

# print(emp_details)

# yoj = emp_id[4:8]
# loc = emp_id[9:12]
# e_id = emp_id[13:]

# emp_info = ""
# for e in emp_details:
#     emp_info += "".join(e)

# print(emp_info)

# List
# empty_list = []
# list1 = [12, 23, "hello", "world", 3.14, True, None]

# print(list1)

# fruits = ["banana", 'apple', 'orange']
# print("Fruits: ", fruits)

# fruits.append('pineapple')
# print("Fruits (append): ", fruits)

# fruits.insert(1, 'avocado')
# print("Fruits (insert): ", fruits)

# fruits.extend(['strawberry', 'grapes'])
# print("Fruits (extend): ", fruits)

data = [("Alice", "HR", 56000), ("Bob", "IT", 65000), ("Charles", "IT",67500), ("Dan", "Development", 78000)]

it_team = []

for e in data:
    if e[1] == "IT":
        it_team.append(e)

print("IT Team: ", it_team)
