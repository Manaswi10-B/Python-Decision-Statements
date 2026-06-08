marks = float(input("Enter marks: "))
if marks > 75:
    print("Distinction")
elif marks > 60:
    print("First Class")
elif marks > 55:
    print("Higher Second Class")
elif marks > 50:
    print("Second Class")
elif marks >= 40:
    print("Pass Class")
else:
    print("Fail")