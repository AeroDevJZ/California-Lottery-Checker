# square brakets means list
nums = [25, 12, 36, 95, 14]
print(nums)
print(nums[0])
print(nums[-1])

names = ["John", "Luke", "Pikard"]
print(names)

# python allows list with different types
values = [9.5, "Navin", 25]
print(values)

# Append adds the value to the end of the list
nums.append(45)
print(nums)

# insert adds the value to the index given shifitng everything else down
nums.insert(2, 77)
print(nums)

# remove searches the list from (0 - the end) and removes the first value that matches what is passed
nums.remove(14)
print(nums)

# removes either last in the list if no parameter given or the value at the index given
nums.pop(1)
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

print(nums[1:2])
