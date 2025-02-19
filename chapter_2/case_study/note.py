import datetime

class Note():
    def __init__(self, id, note_content = "", tags = ""):
        """
        Parameters
        ----------
        id : int
            Identifies each note, must be different for each one note.
        note_content : str, optional
            Note's content. The default is "".
            
        tags: str
            Contains tags associated to the note for searching purposes.
            The tags are stored in a single string variable and separated by
            commas.

        Returns
        -------
        None.

        """
        self.creation_date = datetime.date.today()
        self.id = id
        self.note_content = note_content
        self.tags = tags
    
    def get_creation_date(self):
        """
        Returns the creation date of the note.
        """
        return(self.creation_date)

    def get_id(self):
        """
        Returns the id of the note.
        """
        return(self.id)
    
    def get_note(self):
        """
        Returns the note's content.
        """
        return(self.note_content)
    
    def get_tags(self):
        """
        Returns the tags associated with the note.
        """
        return(self.tags)
    
    def add_tags(self, new_tag, append = True):
        """
        Adds a new tag to the tags variable.

        Parameters
        ----------
        new_tag : str
            Contains the new tag to be added.

        Returns
        -------
        None.

        """
        # If the tag passed as parameter is not string, it convert's into it
        if (type(new_tag) != str):
            new_tag = str(new_tag)
        
        if not append or len(self.tags) == 0:
            self.tags = new_tag
        else:
            self.tags += ("," + new_tag)
                
        
    def reset_note(self):
        """
        Changes the value of the note_content variable to the empty string "".

        Returns
        -------
        None.
        """
        self.note_content = ""
    
    def add_note_content(self, new_content = "", replace = False):
        """
        Adds the value of the variable new_content to the existing one in 
        the variable note_content.

        Parameters
        ----------
        new_content : str, optional
            New content for the note. The default is "".
            
        replace : bool, optional
            If True replaces the whole content of the note

        Returns
        -------
        None.

        """
        if replace:
            self.note_content = new_content
        else:
            self.note_content += new_content
        
        
    def print_note(self):
        """
        Prints the content of a note object.

        Returns
        -------
        None.

        """
        print("---------------------------------------")
        print("id:", self.get_id())
        print("creation date:", self.get_creation_date())
        print("note content:\n", self.get_note())
        print("tags:", self.get_tags())
        print("---------------------------------------")
        
        
