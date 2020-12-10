cars = ['Toyota', 'bmw', 'chevy']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())

number = 0
while number <= 3:
    print(number)
    number = number + 1


def check_toyota(arr):
    for c in cars:
        if c.lower() == 'toyota':
            print('Great! You own a toyota')
            break


check_toyota(cars)
