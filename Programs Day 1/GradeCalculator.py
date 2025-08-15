sub1 = int(input("Enter marks of subject 1 -> "))
sub2 = int(input("Enter marks of subject 2 -> "))
sub3 = int(input("Enter marks of subject 3 -> "))
sub4 = int(input("Enter marks of subject 4 -> "))
sub5 = int(input("Enter marks of subject 5 -> "))

totalMarks = sub1+sub2+sub3+sub4+sub5
percent = (totalMarks/500)*100
grade = ""

if (percent>=90 and percent <= 100):
    grade = "A"
elif (percent>=80 and percent <= 89):
    grade = "B"
elif (percent>=70 and percent <= 79):
    grade = "C"
elif (percent>=60 and percent <= 69):
    grade = "D"
else:
    grade = "F"

print("Your Grade is",grade)