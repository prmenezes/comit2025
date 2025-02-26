class Person:
    """ A person"""

    def __init__(self, f_name, l_name):
        """Class representing a person

        Args:
            f_name (str): First name
            l_name (str): last name
        """
        self.first_name = f_name
        self.last_name = l_name

        self.__super_private  = "private"        
        self._protected_var  = "protected"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self) -> str:
        return f"First Name: {self.first_name} Last Name: {self.last_name}"
    
class Student(Person):
    def __init__(self, f_name, l_name, student_number: int):
        """Class representing a person

        Args:
            f_name (str): First name
            l_name (str): last name
            student_number(int): Student number
        """
        super().__init__(f_name, l_name)
        self.sn = student_number

    def __str__(self):
        return f"Student number {self.sn} -> {super().__str__()}"

    
    

    def print_super_private(self):
        print(self.__super_private)

    def print_protected_var(self):
         print(self._protected_var)



stu_1 = Student("Billy", "Bob", 1)

print(stu_1)
#private variAbles CANNOT BE ACCESSED EXCEPT FROM INSIDE THE CLASS WHERE IT IS DEFINED
#stu_1.print_super_private()
stu_1.print_protected_var()

