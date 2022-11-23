from random import randint

lower_bound = -1
while lower_bound < 0:
    try:
        lower_bound = int(input('Enter the lower bound: '))
    except ValueError:
        print('Incorrect integer. Try again')

upper_bound = -1
while upper_bound < lower_bound:
    try:
        upper_bound = int(input('Enter the upper bound: '))
    except ValueError:
        print('Incorrect integer. Try again')
        continue
    if upper_bound < lower_bound:
        print(f"Upper bound of {upper_bound} can't be lower than lower bound of {lower_bound}. Try again")

print(randint(lower_bound, upper_bound))
