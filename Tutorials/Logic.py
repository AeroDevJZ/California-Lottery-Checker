temperature = 15
if temperature > 30:
    print("It's Hot")
elif temperature > 20:
    print("It's Nice")
else:
    print("It's Cold")
print("Done")

# Turnary Opperator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Faster way to do comparison opperators
if 18 <= age < 63:
    print("Eligible")
