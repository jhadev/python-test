import math

print("python")
print("python " * 10)

x, y = 1, 2
z = 16
unit_price = 3

print(unit_price * y * z)

students_count = 1000
print(type(students_count))

rating = 4.99
print(type(rating))

is_published = False
print(type(is_published))

course_name = """Python
Programming"""

print(type(course_name))

print(len(course_name))
print(course_name[0:3])
print(course_name[-2])

first = "Joe"
last = "Boxer"
full = f"{first} {last}"
print(full)

o = y ** 10
print(o)


# comment
# \" escape sequences
# \'
# \\
# \n

# uppercase variables to tell others its a constant
PI = 3.14159265359
print(math.floor(PI))

p = (math.ceil(PI))
print(p)

b = input("x: ")

print(int(b))
print(float(b))
print(bool(b))

aapl = 165.48

if aapl >= 160:
    message = "above low"
else:
    message = "below low"

print(message)

message = "Above Low" if aapl >= 160 else "Below Low"

print(message)

for x in "Python":
    print(x)

for x in range(0, 10, 2):
    print(x)

stocks = ["AAPL", "GOOG", "TWTR", "NFLX"]
for stock in stocks:
    if stock.startswith("A"):
        print("Found")
        break
else:
    print("Not Found")

guess = 0
answer = 9

while answer != guess:
    guess = int(input("Guess: "))
else:
    pass
