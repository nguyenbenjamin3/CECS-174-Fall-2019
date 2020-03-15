import math


def cost_of_gas():
    c1mileage=float(input('Car 1\'s mileage:'))
    while c1mileage<1:
        c1mileage = float(input('Car 1\'s mileage:'))
    c1fc=float(input('Car 1\'s average fuel cost per gallon:'))
    while c1fc<1:
        c1fc = float(input('Car 1\'s average fuel cost per gallon:'))
    c2mileage=float(input('Car 2\'s mileage:'))
    while c2mileage<1:
        c2mileage = float(input('Car 2\'s mileage:'))
    c2fc=float(input('Car 2\'s average fuel cost per gallon:'))
    while c2fc<1:
        c2fc = float(input('Car 2\'s average fuel cost per gallon:'))
    avg_distance=float(input('Car 2\'s average distance driven each month, in miles:'))
    while avg_distance<1:
        avg_distance = float(input('Car 2\'s average distance driven each month, in miles:'))

    if (c1mileage)and (c1fc) and (c2mileage) and (c2fc) and (avg_distance) >0:
        C1cost_per_year=(avg_distance/c1mileage)*c1fc*12
    #print('Car 1\'s cost per year:', C1cost_per_year)
        C2cost_per_year = (avg_distance / c2mileage) * c2fc * 12
    #print('Car2\'s cost per year:', C2cost_per_year)
        if C1cost_per_year < C2cost_per_year:
            difference = C2cost_per_year-C1cost_per_year
            print('Car 1 costs less to drive per year by $', '%.2f' % difference)
        elif C2cost_per_year<C1cost_per_year:
            difference = C1cost_per_year-C2cost_per_year
            print('Car 2 costs less to drive per year by $', '%.2f' % difference)
        else:
            print('Both cars cost the same amount.')

def used_value():
    orig_price = float(input('Enter original price:$'))
    while orig_price<1:
        orig_price = float(input('Enter original price:$'))

    car_years = int(input('How many years have you had the car?'))
    while car_years<2:
        car_years = int(input('How many years have you had the car?'))

    if orig_price and car_years >0:
        for year in range(car_years):
            orig_price -= orig_price*(.18)
            print('The car is worth $','%.2f'% orig_price)

def stopping_distance():
    initial_speed = float(input('Enter initial speed:'))
    while initial_speed<1:
        initial_speed = float(input('Enter initial speed:'))

    while True:
        try:
            condition_number = int(input('Enter number between 1 and 3 for the condition of you tires (1 is new and 3 is bad)'))
            while condition_number<1:
                condition_number = int(input('Enter number between 1 and 3 for the condition of you tires (1 is new and 3 is bad)'))

        except ValueError:
            condition_number = int(input('Enter number between 1 and 3 for the condition of you tires (1 is new and 3 is bad)'))
        if condition_number < 1 or condition_number > 3:
            continue
        else:
            break

    if initial_speed and condition_number >0:
        while condition_number not in [1, 2, 3]:
            int(input('Enter number between 1 and 3 for the condition of you tires (1 is new and 3 is bad)'))
    if condition_number == 1:
        mu =.8
    elif condition_number ==2:
        mu=.6
    elif condition_number ==3:
        mu=.5

    v = (initial_speed*5280)/3600
    g = 32.174
    d = (v*v)/(2*mu*g)
    print('The car will travel','%.2f' %d,'miles before stopping.')
choice = 0

while choice != 4:
    print('Choose a function!')
    choice = int(input('Main Menu:\n 1. Cost of Gas\n 2. Used Value \n 3. Stopping Distance\n 4. Quit'))
    if choice ==1:
       cost_of_gas()
    elif choice ==2:
        used_value()
    elif choice ==3:
        stopping_distance()
    elif choice ==4:
        print('Bye!')







