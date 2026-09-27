# bug_hunt.py
# Fixed version - prints "Sum of 1 to 5 is: 15"

count = 1
total = 0

# BUG: Missing colon at the end of the 'while' line. Python needs ':' to
#      start the loop body. Fixed by adding ':' at the end.
# BUG: The condition 'count < 5' stopped the loop before adding 5, giving
#      10 instead of 15 - no error, just a wrong answer. Fixed by changing
#      it to 'count < 6' so 1 through 5 are all added.
while count < 6:
    total = total + count
    count = count + 1

# BUG: 'total' is an integer and cannot be joined to a string with '+'.
#      This raised a TypeError. Fixed by converting it with str().
print("Sum of 1 to 5 is: " + str(total))
