class Triangle:
    count = 0  # will be used to keep track of number of objects(triangles) created

    # Python's float = 64-bit double-precision number
    # *args allows a function or constructor to accept 'n' number of positional arguments as a tuple
    def __init__ ( self, *args ):

        # Case 1: Default(/null) constructor/No arguments entered -> All sides equal to 1.0
        if len (args) == 0:
            self._sideA = 1.0
            self._sideB = 1.0
            self._sideC = 1.0

        # Cases 2 and 5 both require 1 argument/parameter
        elif len (args) == 1:

            # Case 5: Constructor that accepts a reference to an existing triangle and clones/copies it
            if isinstance (args [ 0 ], Triangle):  # isinstance(object, class) checks if the object already exists previously
                self._sideA = args [ 0 ].sideA
                self._sideB = args [ 0 ].sideB
                self._sideC = args [ 0 ].sideC

            # Case 2: One-parameter constructor which accepts a double and creates an equilateral triangle equal to the passed argument
            else:  # If argument is a number instead of a Triangle object
                self._sideA = float (args [ 0 ])
                self._sideB = float (args [ 0 ])
                self._sideC = float (args [ 0 ])

        # Case 3: Two-parameter constructor which accepts two floats x and y creates isosceles triangle with sides x,x,y
        elif len (args) == 2:
            self._sideA = float (args [ 0 ])
            self._sideB = float (args [ 0 ])
            self._sideC = float (args [ 1 ])

        # Case 4: Three-parameter constructor which accepts three floats x,y, and z creates scalene triangle with sides x,y,z
        elif len (args) == 3:
            self._sideA = float (args [ 0 ])
            self._sideB = float (args [ 1 ])
            self._sideC = float (args [ 2 ])

        else:
            raise ValueError ("A 'TRI'angle with 4 sides??")

        Triangle.count += 1  # increases count by 1 after an object/triangle is created

    # Using decorators such as "Property" that treat attributes as functions for encapsulation
    # GETTER & SETTER for sideA using 'property' decorator
    @property  # GETTER (has no other arguments than 'self')
    def sideA ( self ):
        return self._sideA

    @sideA.setter  # SETTER -> Triangle1.sideA = 9
    def sideA ( self, value ):
        self._sideA = float (value)

    # GETTER & SETTER for sideB using 'property' decorator
    @property  # GETTER (has no other arguments than 'self')
    def sideB ( self ):
        return self._sideB

    @sideB.setter  # SETTER -> Triangle2.sideB = 11
    def sideB ( self, value ):
        self._sideB = float (value)

    # GETTER & SETTER for sideC using 'property' decorator
    @property  # GETTER (has no other arguments than 'self')
    def sideC ( self ):
        return self._sideC

    @sideC.setter  # SETTER -> Triangle3.sideC = 88
    def sideC ( self, value ):
        self._sideC = float (value)

    # objectCount() method for keeping count of all objects created
    @classmethod
    def objectCount ( cls ):
        return cls.count

    # perimeter() method that calculates and returns perimeter of Triangle
    def perimeter ( self ):
        return self._sideA + self._sideB + self._sideC

    # isRightAngled() method that checks if the triangle is Right-angled triangle or not
    def isRightAngled ( self ):
        a, b, c = sorted ([ self._sideA, self._sideB, self._sideC ])  # Storing all the sides as variables in a SORTED ARRAY for the biggest (HYPOTENUSE)
        return round (a ** 2 + b ** 2, 5) == round (c ** 2, 5)  # Applying PYTHAGORAS THEOREM -> a^2 + b^2 = c^2 ('round' used to avoid decimal issues)

    # toString() method which displays string representation of object
    def __str__ ( self ):
        return f"Sides of triangle : A = {self._sideA} , B = {self._sideB} , C = {self._sideC}"
