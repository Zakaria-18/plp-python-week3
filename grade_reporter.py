# grade_reporter.py
# Grades the five scores, counts passes and fails, and prints the average.

scores = [72, 45, 90, 61, 38]

# Counters and total, worked out by the code
passed = 0
failed = 0
total = 0

# 1. Loop through every score in the list
for score in scores:
    # 2. Work out the grade with if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # 3. Print each score with its grade on its own line
    print(f"Score: {score} - Grade: {grade}")

    # 4. Count passes (50 or more) and fails
    if score >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

    # 5. Add up all the scores
    total = total + score

# Print the pass count and fail count
print(f"Passed: {passed}")
print(f"Failed: {failed}")

# 5. Print the average, rounded to one decimal place
average = total / len(scores)
print(f"Average: {round(average, 1)}")
