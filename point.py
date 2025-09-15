# Create a Point class that has instance variables for x and y-coordinates (you do this in the __init__() method)
# Point should also have a __str__() method that prints out the Point in the format: (x, y)
# Create a distance() function outside of the Point class
# distance() should have 2 Point object parameters: p1, p2
# distance() should return the distance (using the distance formula) between p1 and p2
# Outside of classes and functions, you will write the following program:
# Instantiate 2 Point objects and reference them as point1 and point2. You may decide on their initial values as long as they're non-zero
# Print out both Point objects (and you should see them match the defined format above)
# Print out the distance between the objects using the distance formula. Please make the output descriptive: "The distance between (X1, Y1) and (X2, Y2) is ZZZZ"
# Note: X1, Y1, X2, Y2 should be the actual test values of point1 and point2 and not simply letters

# Submission:
# Record a demonstration that shows BOTH your code and that it works with some sample data 

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __str__(self):
        return (f"({self.x}, {self.y})")
    
#d = √(x₂ - x₁)² + (y₂ - y₁)²
def distance(p1: Point, p2: Point):
    distance = ( (p2.x - p1.x)**2 + (p2.y - p1.y)**2 )**(1/2)
    return distance

point1 = Point(2,9)
point2 = Point(-1,4)

print(point1)
print(point2)
print(f"The distance between {point1} and {point2} is " + str(distance(point1, point2)))
