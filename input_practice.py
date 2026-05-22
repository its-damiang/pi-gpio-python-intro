name = input("What is your name? ")

hours_text = input("How many hours of homework do you usually have in a week? ")

hours = int(hours_text)

print("Nice to meet you,", name + "!")
print("You said you have", hours, "hours of homework per week.")

class_hours = int(input("How many hours per week do you spend on this class? "))

percent = (class_hours / hours) * 100

print("This class is about", percent, "percent of your homework time.")
