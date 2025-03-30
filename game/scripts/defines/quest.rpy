init python:
    import renpy.store as store
    import renpy.exports as renpy

    ## This is the Quest Class that is used to store the quest's information
    class Quest (store.object):
        ## When the variable is created, the information such as 
        ## name, description, available and completed will be set
        def __init__(self, name, description, started = False, completed = False, cancelled = False, failed = False):
            self.name = name
            self.description = description
            self.started = started
            self.completed = completed
            self.cancelled = cancelled
            self.failed = failed
