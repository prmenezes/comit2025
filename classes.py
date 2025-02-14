""" Module containing examples of basic class definitions"""


class Example:
    
    class_variable = "Hello World"

    #Self is mandatory 1st parameter of a METHOD
    #Self is Local Reference variable to the object that is calling the method
    def know_thyself(self):
        print(self)

    def __init__(self, message):
        self.message = message


example1 = Example("Yo")
example2 = Example("LOL")









