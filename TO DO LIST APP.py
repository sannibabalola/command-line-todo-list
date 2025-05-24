# This is a TO DO LIST app using list, loops, if statement.

import sys
from colorama import init, Fore
init(autoreset=True)

# This function loads the file


def load_tasks():
    try:
        with open('my_task.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


# This function save tasks on exit
def save_tasks(my_list):
    with open('my_task.txt', 'w') as f:
        for task in my_list:
            f.write(task + '\n')


# At the start of your program the function is called
my_list = load_tasks()

# Checks the option to decide which operation to perform

# This function adds item to the To do list


def add_item():

    while True:

        add_my_item = input(
            'Enter a task to the to do list or \'done\' to exit: ')
        if add_my_item.lower() == 'done':
            break
        my_list.append(add_my_item)
        print(Fore.GREEN + add_my_item + ' has been added to your TO DO List')

# This function displays the TO DO list


def display_todo():
    if my_list == []:
        print(Fore.YELLOW + 'Your TO DO list is empty')
    else:
        print(Fore.YELLOW + 'Your TO DO list')
        for item in range(len(my_list)):
            print(str(item+1) + ' ' + my_list[item])

# This function displays the TO DO list


def mark_completed_task():
    # Validating the input before removing an item
    while True:
        try:
            mark_option = int(input(
                Fore.BLUE + 'Enter the number of the task you want to mark as completed: '))
            if 1 <= mark_option <= len(my_list):
                break
        except ValueError:
            print('Your input is invalid, please enter a valid number on your TO DO list')
        except IndexError:
            print('Your input is invalid, Enter a number on your TO DO list')
    print(Fore.BLUE + 'Completed Task(s)')
    remove_mark_task = my_list.pop(mark_option-1)
    print(Fore.BLUE + remove_mark_task + ' has been marked as completed')

 # This function remove item from the TO DO list


def remove_item():
    if my_list == []:
        print(Fore.RED + 'Your TO DO list empty')
    else:
        # Validating the input before removing an item
        while True:
            try:
                remove_option = int(
                    input(Fore.RED + 'Enter the number of the item you want to remove from the list:'))
                if 1 <= remove_option <= len(my_list):
                    break
            except ValueError:
                print(
                    'Your input is invalid, please enter a valid number on your TO DO list')
            except IndexError:
                print('Your input is invalid, Enter a number on your TO DO list')
        removed_en_item = my_list.pop(remove_option-1)
        print(Fore.RED + removed_en_item + ' ' + 'has been removed')


# While loop keeps showing menu until program is exited by entering 5
while True:
    # This displays menu option to users

    print('\n' + Fore.CYAN + 'Main Menu')
    print('1: ' + Fore.GREEN + 'Add a new task')
    print('2: ' + Fore.YELLOW + 'Display all tasks')
    print('3: ' + Fore.BLUE + 'Mark a task as completed')
    print('4: ' + Fore.RED + 'Delete a task')
    print('5: ' + Fore.MAGENTA + 'Exit the program')

    # This allows user to enter an option.
    while True:
        try:
            my_option = int(input('Choose an option: '))
            if 1 <= my_option <= 5:
                break
            else:
                print(Fore.CYAN + 'Invalid option. Enter any option from 1 to 5')
        except ValueError:
            print(Fore.CYAN + 'Only valid numbers is allowed')


# This calls funtion to add item to the TO DO list
    if my_option == 1:
        add_item()
# This calls funtion to display the TO DO list
    elif my_option == 2:
        display_todo()

# This calls funtion to mark task as completed
    elif my_option == 3:
        mark_completed_task()

# This calls funtion to remove item from the TO DO list
    elif my_option == 4:
        remove_item()

# This calls funtion to save and exit the app
    elif my_option == 5:
        save_tasks(my_list)
        print(Fore.MAGENTA + 'Exiting program')
        sys.exit()
