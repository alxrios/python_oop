import note


class Notebook():
    def __init__(self, how_many):
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
        self.notes = [] # Container for the notes in the notebook object
        self.how_many = how_many
        for i in range(1, how_many + 1):
            self.notes.append(note.Note(i))
            
    def print_all_notes(self):
        for i in range(0, self.how_many):
            self.notes[i].print_note()
    



