###############################################################################
# Case study of the chapter 2 of the book Python Object Oriented Programming. #
# The case consists in a notebook application.                                #
###############################################################################

import notebook
    
def read_option(min = 1, max = 9, mode = 1):
    """
    Ask the user to introduce an integer between min and max.

    Parameters
    ----------
    min : int, optional
        Minimum number to be acepted as a valid option. The default is 1.
    max : int, optional
        Maximum number to be acepted as a valid option, optional. 
        The default is 9.
    mode : int, optional
        Chose the format of the dialog. 1 for option and 2 for id version.
        The default value is 1.
        
    Returns
    -------
    int value with a valid option between min and max. For every other case
    it prints an error message, and ask for another input.

    """
    modeDict = {1: "option", 2: "id"}
    finish = False
    option = input("Choose an " + modeDict[mode] + ": ")
    while not finish:
        # option = input("Choose an option: ")
        while type(option) != int:
            try:
                option = int(option)
            except:
                option = input("Your " + modeDict[mode] + 
                               " should be an integer between " + 
                               str(min) + " and " + str(max) + 
                               ".\nPlease choose a valid " + modeDict[mode] +
                               ": ")
        # finish = True
        if option < min or option > max:
            option = input("Your " + modeDict[mode] + " should be between " 
                           + str(min) + " and " + str(max) + 
                           "\nPlease choose a valid " + modeDict[mode] + ": ")
        else:
            finish = True
    return(option)

def switchAppend(input_append):
    """
    Changes the format of the input passed as parameter from y/n to True/False.
    If not match anything, it returns True by default, so note's information is
    not missed.

    Parameters
    ----------
    input_append : str
        Option chosen when user is asked to append or not the new content
        to the existing one in the note to be modified.

    Returns
    -------
    False if input_append takes the values n, N, no, No, nO or NO and True
    for any other case.

    """
    input_append = input_append.lower()
    transform = True
    if input_append == "n" or input_append == "no":
        transform = False
    return(transform)


def read_tags(old_tags = "", append = True):
    """
    Helps to read new tags from the user.

    Parameters
    ----------
    old_tags : str, optional
        Old tags present in the note. Useful if the user wants
        to conserve them. The default is "".
    append : bool, optional
        If True the function adds the new tags to the ones
        passed in the first parameter. The default is True.

    Returns
    -------
    str, all the tags in a single string and separated by commas.

    """
    # If append parameter is True old tags are conserved
    if append:
        new_tags = old_tags
    else:
        new_tags = ""
    # If tags are less than ten we can ask the user to add another.
    if len(new_tags.split(',')) < 10:
        single_tag = input("Introduce a new tag: ")
        if len(new_tags.split(',')) > 1 or len(new_tags) > 0:
            new_tags += ("," + single_tag)
        else:
            new_tags += single_tag
    # While the registered tags don't exceed the maxiumum of ten or the user
    # don't tells explicitly that they don't want to add more tags, the 
    # function still asking to introduce more tags.
    ask = True
    while ask and len(new_tags.split(',')) < 10:
        ask = switchAppend(input("Do you want to add another tag? (y/n): "))
        if ask:
            single_tag = input("Introduce a new tag: ")
            new_tags += ("," + single_tag)
    return(new_tags)


def main():
    message = "List of options:\n----------------\n1.Print all notes in the \
notebook.\n2.Print one note.\n3.Modify the content of a note.\n\
4.Modify the tags of a note.\n5.Print notebook's size.\n6.Add a new note \
at the end of the notebook. (Only available if notebook is smaller than 100).\
    \n7.Delete note.\n9.End program.\n"
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
            print("Which note do you want to print?: \
(introduce note's id) ")
            note_id = read_option(max = new_notebook.size(), mode = 2)
            new_notebook.print_single_note(int(note_id))
            print("\n", message)
        elif chosen_option == 3:
            print("Introduce the note's id you want to modify.")
            note_id = read_option(max = new_notebook.size(), mode = 2)
            content = input("Write here the note content: ")
            append = input("Do you want to append the content to the\
 existing one? (y/n): ")
            new_notebook.modify_note_content(note_id, content, 
                                             False if switchAppend(append) 
                                             else True)
            print("\n", message)
        elif chosen_option == 4:
            print("Which note tags do you want to modify?")
            note_id = read_option(max = new_notebook.size(), mode = 2)
            print("The current tags are: ", new_notebook.get_tags(note_id))
            append = switchAppend(input("Do you want to keep the existing\
tags? (y/n): "))
            new_tags = read_tags(new_notebook.get_tags(note_id), append)
            new_notebook.modify_note_tags(note_id, new_tags, False)
            print("\n", message)
        elif chosen_option == 5:
            print("The size of the notebook is:", new_notebook.size())
            print("\n", message)
        elif chosen_option == 6:
            input_content = input("Introduce content of the note: \n")
            input_tags = read_tags()
            new_notebook.add_note(input_content, input_tags)
            print("\n", message)
        elif chosen_option == 7:
            note_id = read_option(1, new_notebook.size(), 2)
            new_notebook.delete_note(note_id)
            print("\n", message)
            
            
            
            

if __name__ == "__main__":
    main()
    
