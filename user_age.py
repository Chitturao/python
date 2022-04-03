try:
    age=int(input('age:'))
    print(age)
    income=20000
    risk=income/age
except ZeroDivisionError:
    print("age cann't be zero")
except ValueError:
    print("Invalid Input")