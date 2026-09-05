students = [
    ("Rahul", 80),
    ("Anil", 95),
    ("Kiran", 70),
    ("Suresh", 85)
]

result = sorted(
    students,
    key=lambda x: x[1],
    reverse=True
)

print(result)

