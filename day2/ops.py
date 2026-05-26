# arithematic operator, assignment, relational, logical 

# arithmetic operators
# total_sales = 20000
# num_regions = 4
# tax_rate = 0.18

# avg_per_region = total_sales / num_regions #division
# region_floor = total_sales // num_regions  # floor division
# tax_amount = total_sales * tax_rate 
# compound_interest = 1000 * (1 + 0.08) ** 5 # exponention

# print(f"Avg Per Region: {avg_per_region}")
# print(f"Tax on Sales: {tax_amount}")
# print(f"Investment: {compound_interest: .2f}")
# print(f"Region Floor: {region_floor}")

# compound assignment operators:
# daily_sales = [1200, 1500, 2200, 900]
# total_sales = 0

# # walrus operator (Python 3.8+)
# if (n := len(daily_sales)) > 3:
#     print("Dataset has the necessary amount. Amount is: ", n)
#     for day_sales in daily_sales:
#         total_sales += day_sales  #total_sales = total_sales + day_sales
#         print(f"Running total: {total_sales}")
# else:
#     print("Insufficient data")

# print(f"Final Sales Amount: {total_sales}")

# Relational operators
# name = input("Enter name: ")
total_marks = int(input("Enter total marks"))

match total_marks:
    case x if 90 <= x <=100:
        print("Grade A")
    
    case x if 80 <= x < 90:
        print("Grade B")
    
    case _:
        print("Invalid Grade")


# if 90 <= total_marks <=100:
#     print("Grade: A+")

# elif 80 <= total_marks < 90:
#     print("Grade: A")

# elif 75 <= total_marks < 80:
#     print("Grade: B+")

# elif 65 <= total_marks < 75:
#     print("Grade: B")

# elif 55 <= total_marks < 65:
#     print("Grade: C")

# elif 40 <= total_marks < 55:
#     print("Grade: D")

# else:
#     print("Fail")
