import note


class Notebook():
    def __init__(self, how_many = 1):
        """
        Initialices the list notes with as much empty notes as indicated
        in the "how_many" parameter.
        Parameters
        ----------
        how_many : int, must be bigger or equal than zero.
            Indicates how many notes the list notes must contain.

        Returns
        -------
        None.

        """
        self.__notes = [] # Container for the notes in the notebook object
        self.how_many = how_many
        for i in range(1, how_many + 1):
            self.__notes.append(note.Note(i))
            
    def print_all_notes(self):
        """
        Prints the information of all stored notes.

        Returns
        -------
        None.

        """
        for i in range(0, self.how_many):
            self.__notes[i].print_note()
    
            
    def modify_note_content(self, id, new_content = "", add = True):
        """
        Modifies the content of the note with the id passed as parameter.

        Parameters
        ----------
        id : int
            Id of the note which modification is wanted.
        new_content : str, optional
            The new content to be added or for replacing the current note. 
            The default is "".
        add : bool, optional
            If True function just appends the new content passed as parameter
            to the exisisting one in the note.

        Returns
        -------
        None.

        """
        if not self.__checkId(id):
            print("Error in id parameter. It must an integer from 1 to ", 
                  self.how_many)
        else:
            self.__notes[id - 1].add_note_content(new_content, add)
            
    def modify_note_tags(self, id, new_tags, add = True):
        """
        Modify the existing tags of the note indicated with the id parameter.

        Parameters
        ----------
        id : int
            Id of the note which is wanted to be modified.
        new_tags : str
            New tags to be added or used to replace the current ones.
        add : bool, optional
            If True it add the tags passed in the paramter new_tags. 
            The default is True.

        Returns
        -------
        None.

        """
        if not self.__checkId(id):
            print("Error in id parameter. It must an integer from 1 to ", 
                  self.how_many)
        else:
            self.__notes[id - 1].add_tags(new_tags, add)
            
        
    def __checkId(self, id):
        """
        Checks if id is a positive integer between 1 and the value stored in
        the variable how_many.

        Parameters
        ----------
        id : int
            Note's id.

        Returns
        -------
        True if id is valid, False if not.

        """
        result = True
        if type(id) != int or id < 1 or id > self.how_many:
            result = False
        return(result)
            
        
    def delete_note(self, id):
        """
        Deletes the note corresponding to the id passed as parameter.

        Parameters
        ----------
        id : int
            Note's id.

        Returns
        -------
        None.

        """
        if not self.__checkId(id):
            print("Error in id parameter. It must an integer from 1 to ", 
                  self.how_many)
        else:
            # Check this loop, in doesen't works
            for i in range(id, self.how_many):
                self.__notes[i - 1] = self.__notes[i]
                
            self.__notes.pop()
            self.how_many -= 1


    def add_note(self, new_note_content = "", new_note_tags = ""):
        print("test")

