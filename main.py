from Triangle import Triangle

# Case 1: Default(/null) constructor/No arguments entered -> All sides equal to 1.0
triangle1 = Triangle ()
# Case 2: One-parameter constructor which accepts a double and creates an EQUILATERAL triangle
triangle2 = Triangle (2)
# Case 3: Two-parameter constructor which accepts two floats x and y creates ISOSCELES triangle
triangle3 = Triangle (6, 7)
# Case 4: Three-parameter constructor which accepts three floats x,y, and z creates SCALENE triangle
triangle4 = Triangle (3, 4, 5)
# Case 5: Constructor that accepts a reference to an existing triangle and clones/copies it (COPY CONSTRUCTOR)
triangle5 = Triangle (triangle4)

# OBJECT COUNT
print ("\nTotal object(s)/triangle(s) created = ", Triangle.count)
print ("\n")  # line break

# PERIMETER OF TRIANGLES (1-5)
print ("Perimeter of Triangle 1 = ", triangle1.perimeter ())
print ("Perimeter of Triangle 2 = ", triangle2.perimeter ())
print ("Perimeter of Triangle 3 = ", triangle3.perimeter ())
print ("Perimeter of Triangle 4 = ", triangle4.perimeter ())
print ("Perimeter of Triangle 5 = ", triangle5.perimeter ())
print ("\n")  # line break

# CHECKING FOR RIGHT ANGLED TRIANGLES (1-5)
print ("Is Triangle 1 right-angled => ", triangle1.isRightAngled ())
print ("Is Triangle 2 right-angled => ", triangle2.isRightAngled ())
print ("Is Triangle 3 right-angled => ", triangle3.isRightAngled ())
print ("Is Triangle 4 right-angled => ", triangle4.isRightAngled ())
print ("Is Triangle 5 right-angled => ", triangle5.isRightAngled ())
print ("\n")  # line break

# DISPLAYING ALL OBJECTS AS STRINGS
print ("Triangle 1 ->", triangle1.__str__ ())
print ("Triangle 2 ->", triangle2.__str__ ())
print ("Triangle 3 ->", triangle3.__str__ ())
print ("Triangle 4 ->", triangle4.__str__ ())
print ("Triangle 5 ->", triangle5.__str__ ())
print ("\n")  # line break

# EXAMPLE OF GETTER
print("Displaying sideC of triangle4 using getter :",triangle4.sideC)
print ("\n")  # line break

# EXAMPLE OF SETTER
triangle4.sideA = 88
triangle4.sideB = 99
triangle4.sideC = 1010
print("Displaying all the altered sides using setters",triangle4.__str__())