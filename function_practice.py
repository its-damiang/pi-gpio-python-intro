def percent_of(homework_hours, class_hours):
    percent = (class_hours / homework_hours) * 100
    return percent

def greeting(name):
    print("Hello", name + "!")

name = input("What is your name? ")

total_hours = int(input("Total homework hours per week: "))

class_hours = int(input("Hours per week for this class: "))

greeting(name)

result = percent_of(total_hours, class_hours)

print("This class is about", result, "percent of your homework time.")
