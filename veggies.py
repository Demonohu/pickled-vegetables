# Pickled Vegetables
# Write a program that keeps vegetable names and prices in a dictionary as key-value pairs. 
# The program should display a menu that lets the user see a list of all vegetables and their 
# prices, add a new vegetable and price, change the price of an existing vegetable, and delete 
# an existing vegetable and price. The program should pickle the dictionary and save it to a 
# file when the user exits the program. Each time the program starts, it should retrieve the 
# dictionary from the file and unpickle it.

import pickle

def get_menu_choice():
    """
    This function gets a choice from the user and validates it.
    """
    print()
    print('Vegetables and their prices.')
    print('----------------------------')
    print('1. See list of the vegetables and their prices')
    print('2. Add a new vegetable and price')
    print('3. Change the price of a vegetable')
    print('4. Delete a vegetable')
    print('5. Quit program')
    choice = eval(input('Enter a choice: '))

    #Validate the user's input
    while choice not in range(1, 6):
        choice = eval(input('Enter a valid choice! '))

    return choice

def see_list(veggies_list):
    """
    This function displays a list of all vegetables and their prices
    """
    if veggies_list != {}:
        print('Here are the vegetables and their prices.')
        for key in veggies_list:
            print('Vegetable:', key)
            print('Price: $', format(veggies_list[key], ',.2f'), sep='')
            print()
    else:
        print('The dictionary is empty.')

def add(veggies_list, input_file):
    """
    This function allows the user to add a new vegetable to the dictionary
    """
    again = 'y'         #To control the function for repetition
    while again.lower() == 'y' or again.lower() == 'yes':
        #Get the vegetable to be added
        veg = input('Enter the vegetable: ')
        #Get it's price
        price = eval(input("Enter it's price: "))

        #Add the vegetable to the dictionary if it's not already there.
        if veg not in veggies_list:
            veggies_list[veg] = price
            pickle.dump(veggies_list, input_file)
        else:
            print('Vegetable already in dictionary')
        again = input('Do you wanna go again? ')
    else:
        print('Your input has been recorded.')


def change(veggies_list, input_file):
    """
    This function allows the user to change the price of a vegetable
    """
    #Ask the user for the vegetable.
    veg = input('Enter the vegetable: ')
    #Ask the user for the updated price
    price = eval(input('Enter the new price: '))

    #Check for the vegetable in the dictionary and change the price if found.
    if veg in veggies_list:
        veggies_list[veg] = price
        print('The price has been updated.')
        pickle.dump(veggies_list, input_file)
    else:
        print('Vegetable not found.')

def delete(veggies_list, input_file):
    """
    This function allows the user to delete a vegetable
    """
    #Get the vegetable to be deleted.
    veg = input('Enter the vegetable to be deleted: ')

    #Check for the vegetable and delete if found.
    if veg in veggies_list:
        del veggies_list[veg]
        print('The vegetable has been deleted')
        pickle.dump(veggies_list, input_file)
    else:
        print('Vegetable not found.')


def main():
    has_error = False   #To control the exceptions.
    try:
        #Open file for binary reading
        input_file = open('veggies.dat', 'rb')
        veggies_list = pickle.load(input_file)

        choice = 0          #Initialize a variable for the user's choice

        while choice != 5:
            #Get the user's menu choice.
            choice = get_menu_choice()
            
            if choice == 1:
                see_list(veggies_list)
            elif choice == 2:
                add(veggies_list, input_file)
            elif choice == 3:
                change(veggies_list, input_file)
            elif choice == 4:
                delete(veggies_list, input_file)
            else:
                exit
        input_file.close()
    
    except Exception as err:
        has_error = True
        print(err)
        print('An error has occured. The file does not exist')

    finally:
        if has_error:
            veggies_list = {}
            input_file = open('veggies.dat', 'wb')
            choice = 0          #Initialize a variable for the user's choice

            while choice != 5:
                #Get the user's menu choice.
                choice = get_menu_choice()
                
                if choice == 1:
                    see_list(veggies_list)
                elif choice == 2:
                    add(veggies_list, input_file)
                elif choice == 3:
                    change(veggies_list, input_file)
                elif choice == 4:
                    delete(veggies_list, input_file)
                else:
                    exit
            input_file.close()
main()