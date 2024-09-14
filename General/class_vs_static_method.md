Class Method vs Static Method
The basic difference between the class method vs Static method in Python and when to use the class method and static method in Python.

-A class method takes class as the first parameter while a static method needs no specific parameters.

-A class method can access or modify the class state while a static method can’t access or modify it.

-In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.

-We use @classmethod decorator in Python to create a class method and we use @staticmethod decorator to create a static method in Python.