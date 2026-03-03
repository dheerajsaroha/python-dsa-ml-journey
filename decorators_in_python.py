def dheeraj(func):
    def last_name():
        print("Mr.",end = " ")
        func()
        print("Saroha")
    return last_name

@dheeraj
def name():
    print("Dheeraj",end = " ")

name()

# @decorator
# def greet():
#     print("Hello World")
# greet()
