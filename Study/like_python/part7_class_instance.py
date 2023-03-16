class Coord(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

point = Coord(1, 2)
print( '({}, {})'.format(point.x, point.y) ) 

# 또는
def print_coord(coord):
    print( '({}, {})'.format(coord.x, coord.y) )
print_coord(point)

#이걸 __str__ 메소드로 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        #클래스 내부에서 format 지정 가능 
        return '{0}: {1}'.format(self.name, self.age)
    
def main():
    p = Person("jiin", 30)
    print(p) # __str__ 호출 

main()