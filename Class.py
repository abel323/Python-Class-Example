class geometery():
    #Define methodes that can calculate geometrical figures
    
    def rectangle(self,width,length):
        area = length * width
        perimeter = 2 * (length+width)
        print("Area=",area)
        print("Perimeter=",perimeter)
    
    def circle(self,radius):
        area = 3.14 * pow(radius,2.0)
        diameter = 2 * radius
        print("Area=", area)
        print("Diameter=", diameter)


#variables to calculate the 
width = float(input("Enter width: "))
length = float(input("Enter length: "))

radius = float(input("Enter radius: "))

#Create new object from geometery class

geo = geometery()

#Call the methods from geometry class

geo.rectangle(width,length)
geo.circle(radius)
