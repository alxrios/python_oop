###############################################################################
# Case study of the chapter 2 of the book Python Object Oriented Programming. #
# The case consists in a notebook application.                                #
###############################################################################

import notebook

def options(): # Probably this function isn't gonna be used. Delete it.
    """
    Deploys a list of options in the console.

    Returns
    -------
    None.

    """
    print("")
    
def read_option(min = 1, max = 9):
    """
    Ask the user to introduce an integer between min and max.

    Parameters
    ----------
    min : int, optional
        Minimum number to be acepted as a valid option. The default is 1.
    max : int, optional
        Maximum number to be acepted as a valid option, optional. The default is 9.

    Returns
    -------
    int value with a valid option between min and max. For every other case
    it prints an error message, and ask for another input.

    """
    finish = False
    option = input("Choose an option: ")
    while not finish:
        # option = input("Choose an option: ")
        while type(option) != int:
            try:
                option = int(option)
            except:
                option = input("Your option should be an integer between " + 
                               str(min) + " and " + str(max) + 
                               ".\nPlease choose a valid option: ")
        # finish = True
        if option < min or option > max:
            option = input("Your option should be between " + str(min) + 
                           " and " + str(max) + 
                           "\nPlease choose a valid option: ")
        else:
            finish = True
    return(option)


def menu():
    message = "List of options:\n----------------\n1.Print all notes in the \
notebook.\n2.Print one note.\n"
    print("---------------------\nNotebook application.\n---------------------")
    end_program = False
    # In the first run of the code the notebook should be created
    print("How many notes you want in your notebook? (max is 100)")
    notebook_size = read_option(1, 100)
    new_notebook = notebook.Notebook(notebook_size)
    print(message)
    while(not end_program):
        chosen_option = read_option()
        print("Your option choosen is: ", chosen_option)
        if chosen_option == 9:
            end_program = True
        elif chosen_option == 1:
            new_notebook.print_all_notes()
            print("\n", message)
        elif chosen_option == 2:
            new_notebook.print_all_notes()
            print("\n", message)
            
    

def main():
    # testNotebook = notebook.Notebook(7)
    # testNotebook.modify_note_content(1, "This is note one.")
    # testNotebook.modify_note_content(2, "This is note two.")
    # testNotebook.modify_note_content(3, "This is note three.")
    # testNotebook.modify_note_content(4, "This is note four.")
    # testNotebook.modify_note_content(5, "This is note five.")
    # testNotebook.modify_note_content(6, "This is note six.")
    # testNotebook.modify_note_content(7, "This is note seven.")
    # testNotebook.print_all_notes()
    # # Let's check the detetion of some note
    # testNotebook.delete_note(3)
    # testNotebook.print_all_notes()
    menu()
   

if __name__ == "__main__":
    main()
    
    


