import re

text = "Python programming"

result = re.match(r"^Python", text)

if result:
    print("String starts with Python")
else:
    print("Not matched")


import re

text = "My roll number is 12345"

result = re.findall(r"\d+", text)

print(result)

import re

text = "Python12345"

digits = re.findall(r"\d", text)

print("Total digits:", len(digits))

import re

text = "Python is easy to learn"

words = re.findall(r"\w+", text)

print(words)

import re

text = "Python@123#Programming!"

result = re.sub(r"[^A-Za-z0-9]", "", text)

print(result)
