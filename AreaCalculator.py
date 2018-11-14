"""In this project, we'll create a calculator that can compute the area of the following shapes like circle and triangle areas. The program should do the following: Prompt the user to select a shape,  Calculate the area of that shape, Print the area of that shape to the user."""

print "calculator is starting up"

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
    radius = float(raw_input("Enter the radius: "))
    area = float(3.14 * (radius ** 2))
    print "The area of circle is: %s" % (area)

elif option == "T":
    base = float(raw_input("Enter the base of triangle: "))
    height = float(raw_input("Enter the height of triange: "))
    area = float(0.5 * base * height)
    print "The area of traingle is %s" % (area)

else:
    print "You entered invalid input"

print "Exiting...."
