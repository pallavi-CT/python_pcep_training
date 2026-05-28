employees = {
    "E001": {"name": "Rahul", "dept": "Engineering", "salary": 85000, "skills": ["Python", "SQL"]},
    "E002": {"name": "Meena", "dept": "Analytics",   "salary": 92000, "skills": ["R", "Tableau", "SQL"]},
    "E003": {"name": "Dev",   "dept": "Engineering", "salary": 78000, "skills": ["Java", "Python"]},
}

# retrieval
print(employees.get('E002')['name'])
print(employees.get('E003').get('dept'))
print(employees['E001']['skills'])

dept_totals = {}
dept_count = {}

for e in employees.values():
    dept = e['dept']
    dept_totals[dept] = dept_totals.get(dept, 0) + e['salary']
    dept_count[dept] = dept_count.get(dept, 0) + 1

# avg sal by dept
for d in dept_totals:
    avg = dept_totals[d] / dept_count[d]
    print(f" {d} {avg:,.0f}")

