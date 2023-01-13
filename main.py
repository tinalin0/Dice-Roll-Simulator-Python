import random

# Dice Roll Simulator
loop = True
dice1 = 0
dice2 = 0

# Loop until option is 5
while loop == True:
    # Display Menu
    print("\nDice Roll Simulator Menu")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")

    # Input
    option = int(input("Select an option (1-5): "))

    # Process
    if option == 1:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("\n" + str(dice1) + "," + str(dice2) +
              "(sum: " + str(dice1+dice2) + ")")
    elif option == 2:
        for x in range(5):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(str(dice1) + "," + str(dice2) +
                  "(sum: " + str(dice1+dice2) + ")")
    elif option == 3:
        num_times = input("\nHow many rolls would you like? ")
        for x in range(int(num_times)):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(str(dice1) + "," + str(dice2) +
                  "(sum: " + str(dice1+dice2) + ")")
    elif option == 4:
        num_rolls = 0
        while dice1+dice2 != 2:
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(str(dice1) + "," + str(dice2) +
                  "(sum: " + str(dice1+dice2) + ")")
            num_rolls += 1
        print("SNAKE EYES! It only took " +
              str(num_rolls) + " rolls to get snake eyes.")
    elif option == 5:
        loop = False
    else:
        print("That is not an option")
