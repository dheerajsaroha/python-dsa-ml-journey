marks = int(input("Enter marks: "))

def grade(marks):
    result = None
    if marks >= 90:
        result = "A"
    elif marks >= 75 and marks <= 89:
        result = "B"
    elif marks >= 60 and marks <= 74:
        result = "C"
    elif marks < 60:
        result = "Fail"
    return result

print(grade(marks))