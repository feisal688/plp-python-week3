count = 1
total = 0

# BUG: Added a colon (:) after the while condition because Python requires it.
while count <= 5:
    # BUG: Changed the condition from count < 5 to count <= 5
    # so the loop includes the number 5.
    total = total + count

    count = count + 1

# BUG: Converted total to a string using str() because it is an integer
# and cannot be directly concatenated with a string.
print("Sum of 1 to 5 is: " + str(total))