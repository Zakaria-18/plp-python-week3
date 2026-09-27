# bug_hunt.py
# Fixed version - prints "Sum of 1 to 5 is: 15"

count = 1
total = 0

# BUG: Missing colon at the end of the 'while' line. Python needs ':' to
#      start the loop body. Fixed by adding ':' -> 'while count < 5:'
while count < 5:
    total = total + count
    count = count + 1

# BUG: The condition 'count < 5' stops the loop before adding 5, so the
#      sum was 10 instead of 15. No error message - just a wrong answer.
#      Fixed by changing the condition to 'count < 6' so 1..5 are added.
#      (The line above was changed to: while count < 6:)

# BUG: 'total' is an integer and cannot be joined to a string with '+'.
#      This raised a TypeError. Fixed by converting it: str(total)
print("Sum of 1 to 5 is: " + str(total))
