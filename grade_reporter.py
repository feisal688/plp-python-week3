Log in
Sign up for free
You said:
Week 3 Assignment on Conditions and Loops
Description
Grade Reporter & Bug Hunt

Put this week's two big ideas - repeating work with loops and making decisions with conditions - to work in two small programs.

This assignment will help you practice:

Looping through a list with for
Choosing between several outcomes with if / elif / else
Building up a running total or count inside a loop
Reading a while loop and understanding when it stops
Finding a bug that produces no error message at all

Files to create (use these exact names):

grade_reporter.py
bug_hunt.py

GitHub repository name to use (public, exact): plp-python-week3

Your submission for this assignment is one link: your public GitHub repository containing all the files above. Use these exact file and repository names so your submission matches the marking checklist. Part A - Grade Reporter

Create the file grade_reporter.py.

Start your file with this list. Do not change these numbers.

scores = [72, 45, 90, 61, 38]

Use a for loop to go through every score in the list.
Inside the loop, use if / elif / else to work out a grade: 80 and above is A, 70 to 79 is B, 50 to 69 is C, and below 50 is F.
Print each score with its grade on its own line.
Count how many learners passed (a score of 50 or more) and print the number that passed and the number that failed.
Add up all the scores and print the average, rounded to one decimal place round(average, 1).

Every number you print must be worked out by your code. Do not count the passes yourself and type in 3.

Required results:

A working grade_reporter.py that prints a grade for all five scores.
The pass count, the fail count, and the average, all calculated by your program.
Part B - Bug Hunt

Create the file bug_hunt.py and paste in this broken program exactly as shown:

count = 1
total = 0

while count < 5
    total = total + count
    count = count + 1

print("Sum of 1 to 5 is: " + total)



This program is supposed to add up the numbers 1, 2, 3, 4, and 5. The correct answer is 15.

Run the program and read the first error message carefully.
Fix the bugs one at a time, re-running after each fix - this program hides three bugs.
Above each line you fixed, add a comment starting with # BUG: explaining what was wrong and how you fixed it.

Be warned: only two of these bugs produce an error message. The third one lets the program run happily and print an answer that is simply wrong. If your program prints anything other than 15, you still have a bug.

Required results:

A fixed bug_hunt.py that prints Sum of 1 to 5 is: 15.
Three # BUG: comments, one for each bug you found.
Submission Requirements

Your submission is one link to a public GitHub repository.

Create a public GitHub repository named exactly: plp-python-week3
Add all your work. The repository must contain:
grade_reporter.py
bug_hunt.py (with your three # BUG: comments)
README.md - the assignment title, one line describing each file, and 2–3 sentences: which bug in Part B was hardest to find, and how did you know something was wrong when there was no error message?
Submit the repository link on the LMS:

https://github.com/<your-username>/plp-python-week3

Before you submit: open your link in a private/incognito browser window - if you can see the files without logging in, the repo is public, and your instructor can mark it.

ChatGPT said:
Here is a complete solution for your Week 3 Assignment: Conditions and Loops — Grade Reporter & Bug Hunt. You need to create three files and upload them to a public GitHub repository named exactly plp-python-week3.

Part A: grade_reporter.py
This program uses a for loop, if / elif / else, a pass counter, a fail counter, and a running total to calculate the average.

python

scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")

    if score >= 50:
        passed += 1
    else:
        failed += 1

    total += score

average = total / len(scores)

print("Passed:", passed)
print("Failed:", failed)
print("Average:", round(average, 1))
Expected output
text
Score: 72, Grade: B
Score: 45, Grade: F
Score: 90, Grade: A
Score: 61, Grade: C
Score: 38, Grade: F
Passed: 3
Failed: 2
Average: 61.2
Part B: bug_hunt.py
The original program contains three bugs:

The while statement is missing a colon (:), which causes a syntax error.

The loop condition count < 5 stops before adding 5. It must be count <= 5.

The print statement tries to join a string and an integer using +, which causes a type error.

Here is the corrected program with a # BUG: comment above each fixed line.

python

count = 1
total = 0

# BUG: Added the missing colon to the while statement.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Changed < to <= so the loop includes the number 5.
# BUG: Used an f-string to print the integer total with the text.
print(f"Sum of 1 to 5 is: {total}")
Important: The assignment asks for three comments, one for each bug. The code above has the correct three fixes, but the comments should each appear directly above the specific line they explain. Use this final version to make that clearer:

python

count = 1
total = 0

# BUG: Added the missing colon to fix the syntax error.
while count <= 5:
    # BUG: Changed < to <= so the loop includes 5.
    total = total + count
    count = count + 1

# BUG: Used an f-string to avoid adding a string and integer directly.
print(f"Sum of 1 to 5 is: {total}")
Expected output
text
Sum of 1 to 5 is: 15
The second bug is particularly important: the original condition count < 5 does not produce an error, but it calculates only 
1
+
2
+
3
+
4
=
10
1+2+3+4=10. You know something is wrong because the required sum is 15, even though the program runs successfully.

Part C: README.md
Create a third file named README.md with the following content.

Writing


Week 3 Assignment: Conditions and Loops
Files
grade_reporter.py — Uses loops and conditions to assign grades, count passes and failures, and calculate the average score.
bug_hunt.py — Fixes three bugs in a while loop and calculates the sum of numbers from 1 to 5.
Bug Hunt Reflection
The hardest bug to find was the incorrect while loop condition because it did not produce an error message. The program ran successfully but printed 10 instead of the expected answer, 15. I knew something was wrong by comparing the output with the required sum and checking whether the loop included the number 5.

Part D: Create your GitHub repository
Follow these steps to prepare and submit your assignment.

Open 
GitHub  and sign in to your account.

Click the + icon in the top-right corner and choose New repository.

Enter the repository name exactly as shown below.

Repository name

plp-python-week3
Select Public so your instructor can access the repository.

Click Create repository.

Use Add file → Create new file to create each of these files. Paste the corresponding code or README content into each file, then commit the changes.

- grade_reporter.py
- bug_hunt.py
- README.md

Part E: Check your submission
Submission checklist
0 of 7


Repository is named plp-python-week3

Repository visibility is Public

grade_reporter.py produces the correct grades, counts and average

bug_hunt.py prints Sum of 1 to 5 is: 15

bug_hunt.py contains three # BUG: comments

README.md includes the file descriptions and reflection

Repository opens in a private/incognito browser window
Final submission link
Your submission should look like this:

https://github.com/YOUR-USERNAME/plp-python-week3

Replace YOUR-USERNAME with your actual GitHub username, then submit that link on your LMS.

One final tip: In bug_hunt.py, put two separate # BUG: comments immediately above the while count <= 5: line to explain the missing colon and the incorrect loop condition, and one above the print(...) line to explain the string/integer issue. This ensures all three bugs are documented as required.


You said:
give me the codes separately where i can copy them easily

ChatGPT said:
Here are the three files separately, ready for you to copy and paste into your GitHub repository.

1. grade_reporter.py
Copy this code into a file named exactly grade_reporter.py.

python

scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")

    if score >= 50:
        passed += 1
    else:
        failed += 1

    total += score

average = total / len(scores)

print("Passed:", passed)
print("Failed:", failed)
print("Average:", round(average, 1))