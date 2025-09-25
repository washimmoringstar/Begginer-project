import random
playing = True
while playing:
    choice = input('Roll the dice? (yes/no): ')
    if choice == 'yes':
        dice_roll = random.randint(1, 6)
        print(f'You rolled a {dice_roll}')
    elif choice == 'no':
        print('Maybe next time!')
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
