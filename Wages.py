hours = float(input('How many hours did you work this week?:'))
rate = float(input('How much are you paid per hour?:'))

if hours <= 40:
    print('You earned', '$'+'%0.2f' %(float(hours * rate)))

overtime = float(hours - 40)
pay_overtime = (rate * 40  + ((rate * 1.5) * overtime))

if 60 >= hours >= 40:
    print('You earned', '$'+'%0.2f' %(pay_overtime))

superovertime = rate * 40  + (rate * 1.5) * (60 - 40) + (rate * 2.0) * (hours - 60)

if hours > 60:
    print('You earned', '$'+'%0.2f' % (superovertime))
