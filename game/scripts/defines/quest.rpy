init python:
    import renpy.store as store
    import renpy.exports as renpy

    ## This is the Quest Class that is used to store the quest's information
    class Quest (store.object):
        ## When the variable is created, the information such as 
        ## name, description, available and completed will be set
        def __init__(self, name, description, started = False, completed = False, cancelled = False):
            self.name = name
            self.description = description
            self.started = started
            self.completed = completed
            self.cancelled = cancelled


        ## This determines wheter the quest will show in the choices.
        ## A quest will show if it is available and has not been completed.
        @property
        def should_show(self):
            if self.started and not self.completed:
                return True
            return False
