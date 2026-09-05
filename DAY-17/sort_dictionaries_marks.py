students = [
    {"name": "Rahul", "marks": 80},
    {"name": "Anil", "marks": 95},
    {"name": "Kiran", "marks": 70},
    {"name": "Suresh", "marks": 85}
]

result = sorted(students, key=lambda x: x["marks"])
print(result)

