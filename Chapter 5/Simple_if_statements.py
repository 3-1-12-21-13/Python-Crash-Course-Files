# Python's if statement allows you to examine the current state of a program and respond appropriately to that state.
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# The loop in this example first checks if the value of car is 'bmw'. If it is then it prints it in caps. Otherwise it will print the value of car in titlecase instead.