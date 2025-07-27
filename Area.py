class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print('area of the circle is ', self.radius * self.radius)

    def perimeter(self):
        print("Perimeter of the circle is", 2 * 3.14 * self.radius)



mycircle = circle(4)

mycircle.area()
mycircle.perimeter()

