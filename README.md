# PLP Python Week 3 - Grade Reporter & Bug Hunt

## Files
- `grade_reporter.py` - Loops through the scores list, assigns a letter grade with if/elif/else, counts passes and fails, and prints the average.
- `bug_hunt.py` - The fixed version of the broken while-loop program; prints "Sum of 1 to 5 is: 15" with three `# BUG:` comments explaining each fix.

## Reflection
The hardest bug to find was the loop condition `while count < 5`, because it
produced no error message at all - the program ran happily and just printed
the wrong total. I knew something was wrong because the assignment told me the
correct answer should be 15, and my program printed 10, so I traced the loop by
hand and saw that the last value added was 4, not 5. That off-by-one mistake is
exactly the kind of silent bug that only shows up when you check the output
against what you expect, rather than trusting that "no error" means "correct".
