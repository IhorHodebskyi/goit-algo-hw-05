from typing import TypedDict
import re




class Contacts(TypedDict):
    name: str
    phone: str


def parse_input(user_input: str)-> tuple[str, ...]:
    """
    Parse user input into a command and arguments.

    Args:
        user_input (str): The user's input, which may include a command and arguments.

    Returns:
        tuple[str, ...]: A tuple containing the command and any arguments.

    Examples:
         parse_input("hello world")
        ('hello', 'world')
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


     
            
        


def is_valid_contact(contact: Contacts) -> bool:

    """
    Validate a contact dictionary.

    Args:
        contact (Contacts): The contact dictionary to validate.

    Returns:
        bool: True if the contact is valid, False otherwise.

    Notes:
        A contact is considered valid if it has both 'name' and 'phone' keys,
        the 'name' is a non-empty string, and the 'phone' is a 10-digit string.
    """
    if 'name' not in contact or 'phone' not in contact:
        print("Error: Name and phone are required.")
        return False
    

    if not isinstance(contact['name'], str) or len(contact['name']) == 0:
        print("Error: Name should be a non-empty string.")
        return False
    

    if not re.match(r'^\d{10}$', contact['phone']):
        print("Error: Phone number must be 10 digits.")
        return False
    
    return True



def input_error(func):
    """
    Decorator to handle exceptions raised during execution of a function.

    If the decorated function raises a KeyError, IndexError, or ValueError,
    this decorator will catch the exception and return a message prompting
    the user to enter the correct argument for the command.

    Args:
        func: The function to decorate.

    Returns:
        str: The result of the decorated function, or a message prompting the
             user to enter the correct argument for the command.

    Notes:
        This decorator is used to handle exceptions raised when parsing user
        input. It is meant to be used on functions that take arguments from the
        user, and should handle the exceptions that can be raised when the user
        enters invalid input.
    """
    def wrapper(*args, **kwargs):
        text = "Enter the argument for the command"
        try:
            return func(*args, **kwargs)
        except KeyError :
            return  text
        except IndexError:
            return text
        except ValueError:
            return text
    return wrapper



@input_error
def add_contact(value: dict, contacts: list[Contacts])-> str:

    """
    Add a contact to the contact list.

    Args:
        value (dict): The contact dictionary with name and phone number.
        contacts (list[Contacts]): The list of contacts to add the new contact to.

    Returns:
        str: A message indicating whether the contact was added or not.

    Notes:
        The function checks if the provided contact dictionary is valid. If valid,
        it adds the contact to the list if it does not already exist. If the
        contact does not exist, a message is printed.
    """

    
    if not is_valid_contact({"name": value[0], "phone": value[1]}):
        return "Contact invalid"

    if value not in contacts:
        contacts.append({"name": value[0], "phone": value[1]})
        return "Contact added."
    else:
        return "Contact already exists"  
    


@input_error
def change_contact(value: dict, contact_list: list[Contacts])-> str:

    """
    Change the phone number of a contact in the contact list.

    Args:
        value (dict): The contact dictionary with name and phone number.
        contact_list (list[Contacts]): The list of contacts to change the contact in.

    Returns:
        str: A message indicating whether the contact was changed or not.

    Notes:
        The function checks if the provided contact dictionary is valid. If valid,
        it changes the contact in the list if it already exists. If the contact does
        not exist, a message is printed.
    """

    if not is_valid_contact({"name": value[0], "phone": value[1]}):
       return "Contact invalid"
    
    for i, contact in enumerate(contact_list):
        if contact['name'] == value[0]:
            contact_list[i] = {"name": value[0], "phone": value[1]}
            return "Contact updated."
    return "Contact not found."


@input_error
def show_phone(name: str, contact_list: list[Contacts]):

    """
    Display the phone number of a contact in the contact list.

    Args:
        name (str): The name of the contact to display the phone number for.
        contact_list (list[Contacts]): The list of contacts to find the contact in.

    Returns:
        str: A message indicating the phone number of the contact, or a message
             indicating that the contact was not found.

    Notes:
        The function checks if the provided name is valid. If valid, it finds the
        contact in the list and displays its phone number. If the contact does not
        exist, a message is printed.
    """

    for contact in contact_list:
        if contact['name'] == name[0]:
            return f"Phone number for {name[0]}: {contact['phone']}"
        
    return f"Contact {name[0]} not found."





def show_all(contacts: list[Contacts]):
    
    """
    Display all contacts in the contact list.

    Args:
        contacts (list[Contacts]): The list of contacts to display.

    Returns:
        str: A formatted string of all contacts, each with a name and phone number,
             or a message indicating the contact list is empty.
    """

    if not contacts:
        return "Contact list is empty."
    
    result = "\n".join([f"name: {item['name']}, phone: {item['phone']}" for item in contacts])
    return result





def main():
    """
    Main function for the personal assistant bot.

    This function prints a welcome message, then enters a loop where it prompts the user for a command.
    The commands are:

    - add <name> <phone>: Adds a contact with the given name and phone number.
    - change <name> <phone>: Changes the phone number of the contact with the given name.
    - phone <name>: Prints the phone number of the contact with the given name.
    - all: Prints all the contacts.
    - hello: Prints a greeting message.
    - close/exit: Exits the loop and ends the program.

    If the user enters an invalid command, the program prints an error message.
    """
    print("Welcome to the assistant bot!")
    contacts = []

    while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)


            if command in ["close", "exit"]:
                print("Good bye!")
                break

     
            if "add" == command:
                print(add_contact(args, contacts))
            elif "change" == command:
                print(change_contact(args, contacts))
            elif "phone" == command:
                print(show_phone(args, contacts))
            elif "all" == command:
                print(show_all(contacts))
            elif "hello"  == command:
                print("How can I help you?")
            else:
                print("Invalid command.")


if __name__ == "__main__":

    main()