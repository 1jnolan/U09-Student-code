#U09.01.004 More Python:Task 1 p169
# Nested loops
#Student Name:
#***********************************
age=int(input("Please enter your age"))
testScore=int(input("Please enter your test score"))
if age <= 16 and testScore>=80:
    print("Excellent")
elif age>16 and testScore >=80:
    print("Good")
elif testScore <80:
    print("Please try harder next time")
