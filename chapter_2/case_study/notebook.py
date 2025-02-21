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
        self.__how_many = how_many
        for i in range(1, self.__how_many + 1):
            self.__notes.append(note.Note(i))
            
    def print_all_notes(self):
        """
        Prints the information of all stored notes.

        Returns
        -------
        None.

        """
        for i in range(0, self.__how_many):
            self.__notes[i].print_note()
            
    def print_single_note(self, id):
        """
        Prints the information of the corresponding note to the id passed as
        parameter.

        Parameters
        ----------
        id : int
            Note's id.

        Returns
        -------
        Prints the note information in the console.

        """
        self.__notes[id - 1].print_note()
    
            
    def modify_note_content(self, id, new_content = "", replace = False):
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
                  self.__how_many)
        else:
            self.__notes[id - 1].add_note_content(new_content, replace)
            
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
                  self.__how_many)
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
        if type(id) != int or id < 1 or id > self.__how_many:
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
            for i in range(id, self.__how_many):
                self.__notes[i - 1] = self.__notes[i]
                
            self.__notes.pop()
            self.__how_many -= 1
            
    
    def get_tags(self, id):
        """
        Returns the tags of the note corresponding to the id passed as 
        parameter.

        Parameters
        ----------
        id : int
            Id of the note which tags are wanted.

        Returns
        -------
        Returns the string cotaining the note tags.

        """
        return(self.__notes[id - 1].get_tags())


    def add_note(self, new_note_content = "", new_note_tags = ""):
        """
        Adds one note to the end of the notebook if there is space for more
        notes, this is, a notebook of less than 100 notes.

        Parameters
        ----------
        new_note_content : str, optional
            Content of the note to be added. The default is "".
        new_note_tags : str, optional
            Tags of the note to be added. The default is "".

        Returns
        -------
        None.

        """
        if self.__how_many < 100:
            self.__notes.append(note.Note(self.__how_many + 1, 
                                          new_note_content, new_note_tags))
            self.__how_many += 1
        else:
            print("Note wasn't added because notebook is full.")


    def size(self):
        """
        Returns the current notebook size.

        Returns
        -------
        int

        """
        return(self.__how_many)
