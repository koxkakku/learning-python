racer_one = float(input())
racer_two = float(input())
racer_three = float(input())

if racer_one < racer_two and racer_one < racer_three:
    print('racer_one is winner')
elif racer_two < racer_one and racer_two < racer_three:
    print('racer_two is winner')
elif racer_three < racer_one and racer_three < racer_two:
    print('racer_three is winner')
else:
    if racer_one == racer_two:
        print('racer_one and racer_two are equal')
    elif racer_two == racer_three:
        print('racer_two and racer_three are equal')
    elif racer_three == racer_one:
        print('racer_one and racer_three are equal')
    else:
        print('all racers completed in equal time')