lock1 = int(input("What is the first number in the combination?\n"))
lock2 = int(input("What is the second number in the combination?\n"))
lock3 = int(input("What is the third number in the combination?\n"))

if (lock1 <= 39) and (lock1 >= 0) and (lock2 <= 39) and (lock2 >= 0) and (lock3 <= 39) and (lock3 >= 0):
    tick1 = 40 - lock1
    tick2 = abs(lock2 - lock1)
    if lock3 >= lock2:
        tick3 = (40 - lock3) + lock2
    else:
        tick3 = lock3 - lock2
print()

count = 0
while count >= 0:
    g1 = int(input("Turn the lock clockwise by how much?"))
    g2 = int(input("Turn the lock counterclockwise by how much?"))
    g3 = int(input("Turn the lock clockwise by how much?"))
    count = count + 1

    if 0 <= g1 <= 39 and 0 <= g2 <= 39 and 0 <= g3 <= 39:
        if g1 != tick1 or g2 != tick2 or g3 != tick3:
            print('Sorry this sequence is incorrect')
        elif g1 == tick1 and g2 == tick2 and g3 == tick3:
            count = -1
            print()
            break
    else:
        print("Enter values from 0-39")

if count == -1:
    print("Correct! You have won an A in CECS 174.")

