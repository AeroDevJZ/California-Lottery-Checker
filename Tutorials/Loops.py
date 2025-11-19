# number is the equivilent of i = 0 with only 1 number in range
for number in range(3):
    print("Attempt", number, (number + 1) * ".")
# number is initalized as first number in range and loops i += 1 until it reaches the last number and terminates the loop (last num is exclusive)
for i in range(1, 4):
    print("Attempt", i, i * ".")
# for three it goes range(start[inclusive], end[exclusive], i += input) so last is how much i increases by
for i in range(1, 10, 2):
    print("Attempt", i, i * ".")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# If the loop runs all the way through w/o a break, the else statement triggers
successful = True
for i in range(3):
    print("Attempt")
    if successful:
        print("Sucess")
        break
else:
    print("Attempted 3 times and failed")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

for i in range(5):
    for j in range(3):
        print(f"({i}, {j})")

# range is iterable so you can replace it with anything iterable like lists which is what a string is (list of characters)

for i in [1, 2, 3, 4]:
    print(i)
for i in "Python":
    print(i)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

i = 100
while i > 0:
    print(i)
    i //= 2

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
