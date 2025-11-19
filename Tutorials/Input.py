x = input("x: ")

# Returns what data type input is
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

# These methods convert strings into the various data types

int(x)
float(x)
bool(x)
str(x)

# Falsy - "", 0, None  [Everything else is true]

bool(0)  # evaluated as false
bool("False")  # evaluated as true
