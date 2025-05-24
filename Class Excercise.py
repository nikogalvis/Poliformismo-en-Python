from math import acos, degrees

class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y
   
  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y
   
  def reset(self):
    self.x = 0
    self.y = 0

  def __repr__(self):
    return f"Point({self.x}, {self.y})"
   
class Line:
  def __init__(self, start: "Point" = Point(0,0), end: "Point" = Point(0,0)):
    self.start = start
    self.end = end
    self.length = self.line_length()
    self.slope = self.line_slope()

  def vector_addition(self) -> "Line":
    return [self.end.x - self.start.x, self.end.y - self.start.y]
   
  def line_length(self) -> float:
    x = self.vector_addition()
    return ((x[0]**2) + (x[1]**2))**(0.5)
   
  def line_slope(self) ->  float:
    if(self.end.x - self.start.x) == 0:
      return "La pendiente es infinita"
    return (self.end.y - self.start.y)/(self.end.x - self.start.x)
   
  def compute_horizontal_cross(self) -> bool:
    return (self.start.y <= 0) and (self.end.y >= 0)
   
  def compute_vertical_cross(self) -> bool: 
    return (self.start.x <= 0) and (self.end.x >= 0)
   
  def __repr__(self):
    return f"Start: {self.start}  End: {self.end}" 
   
class Shape():
  def __init__(self, is_regular: bool, edge: list[Line], vertice: list[Point]):
    self.edge = Line(start = Point(0,0), end = Point())
    self.is_regular = is_regular
    self.edge = edge
    self.vertice = vertice

  def vertices(self) -> "Point":
    pass
      
  def edges(self) -> "Line":
    pass
      
  def compute_area(self) -> "float":
    pass
      
  def compute_perimeter(self) -> "float":
    pass
      
  def compute_inner_angels(self) -> "float":
    pass
      
class Rectangle(Shape):
  #* Este __init__ tiene muchos datos, para facilitar el proceso de las demás funciones.
  def __init__(self, left_down: "Point", right_up: "Point"):
    super().__init__(is_regular = True, edge = [], vertice = [])
    self.left_down = left_down
    self.right_up = right_up
    self.left_up = Point(self.left_down.x , self.right_up.y)
    self.right_down = Point(self.right_up.x, self.left_down.y)

    self.left_side = Line(start = self.left_down, end = self.left_up)
    self.up_side = Line(start = self.left_up, end = self.right_up)
    self.right_side = (Line(start = self.right_down,
                       end = self.right_up))
    self.down_side = (Line(start = self.left_down,
                      end = self.right_down))
    
    self.width = (float(self.right_up.x)) - (float(self.left_down.x))
    self.height = (float(self.left_up.y)) - (float(self.right_down.y))
      
  #* Como se puede ver aqui, el __init__ hace mas pasables las formulas
  def vertices(self) -> list[Point]:
    return [self.left_up, self.left_down, self.right_down, self.right_up]
    
  def vertices_repr(self) -> list[Point]:
    list_vertices = ["This are the vertices of the rectangle",
                      f"Left Up: {self.left_up}", 
                      f"Left Down: {self.left_down}",
                      f"Right Down: {self.right_down}", 
                      f"Right Up: {self.right_up}"]
    return list_vertices
    
  def edges(self) -> list[Line]:
    return [self.left_side, self.up_side, self.right_side, self.down_side]
    
  def edges_repr(self) -> list[Line]:
    list_edges = ["This are the sides of the rectangle",
                  f"Left Side: {self.left_side}", 
                  f"Top Side: {self.up_side}",
                  f"Right Side: {self.right_side}", 
                  f"Bottom Side: {self.down_side}"]
    return list_edges
    
  #*Dado que es regular, los angulos son iguales y deben completar la ecuación (n-2)*180
  #* En este Caso, los 4 angulos deben completar 360°
  #* Es decir, los angulos son = 360/4
  def compute_inner_angels(self) -> float:
    v1 = [self.left_up.x - self.left_down.x, self.left_up.y - self.left_down.y]
    v2 = [self.right_down.x - self.left_down.x, self.right_down.y - self.left_down.y]
    point_product = v1[0]*v2[0] + v1[1]*v2[1]
    hip1 = ((v1[0]**2)+(v1[1]**2))**0.5
    hip2 = ((v2[0]**2)+(v2[1]**2))**0.5
    if (hip1*hip2) == 0: # Uno de los vectores es nulo, no se puede definir ángulo
      return 90
    degree = point_product/(hip1*hip2)
    angle = degrees(acos(degree))
    return angle

  def inner_angels(self) -> list[float]:
    s = []
    for i in range(len(self.edges())):
      s.append(self.compute_inner_angels())
    return ["Rectangle Angles: "] + s

  def compute_area_repr(self) -> float:
    if (self.width or self.height) < 0:
      return ["Area: "] + [(self.width*self.height)*(0-1)]
    return ["Area: "] + [self.width*self.height]
  
  def compute_area(self) -> float:
    return self.width*self.height
    
  def compute_perimeter_repr(self) -> float:
    return ["Perimeter: "] + [2*(self.width + self.height)]
  
  def compute_perimeter(self) -> float:
    return 2*(self.width + self.height)
    
  def __repr__(self):
    repr = (self.vertices_repr() + self.edges_repr() + self.inner_angels() 
            + self.compute_area_repr() + self.compute_perimeter_repr())
    for i in repr:
      print(i)
    return "That is all i got"

class Square(Rectangle):
  def __init__(self, square_size: float, left_down: "Point"):
    self.size = square_size
    self.left_down = left_down
    self.right_up = Point(self.left_down.x + self.size, self.left_down.y + self.size)
    self.right_down = Point(self.right_up.x,self.left_down.y)
    super().__init__(left_down, self.right_up)

  def vertices_repr(self) -> list[Point]:
    list_vertices = ["These are the vertices of the square",
                      f"Left Up: {self.left_up}", 
                      f"Left Down: {self.left_down}",
                      f"Right Down: {self.right_down}", 
                      f"Right Up: {self.right_up}"]
    return list_vertices

  def edges_repr(self) -> list[Line]:
    list_edges = ["These are the sides of the square",
                  f"Left Side: {self.left_side}", 
                  f"Top Side: {self.up_side}",
                  f"Right Side: {self.right_side}", 
                  f"Bottom Side: {self.down_side}"]
    return list_edges

  def inner_angels(self) -> list[float]:
    s = []
    for i in range(len(self.edges())):
      s.append(self.compute_inner_angels())
    return ["Square Angles: "] + s
    
  def compute_area(self) -> float:
    return self.width**2

  def compute_perimeter(self) -> float:
    return 4*self.width
 
class Triangle(Shape):
  def __init__(self,  point_1 = Point(0,0), point_2 = Point(0,0), point_3 = Point(0,0)):
    super().__init__(is_regular = True, edge = [], vertice = [])
    self.point_1 = point_1
    self.point_2 = point_2
    self.point_3 = point_3

    self.edge_1 = Line(start = self.point_1, end = self.point_2)
    self.edge_2 = Line(start = self.point_2, end = self.point_3)
    self.edge_3 = Line(start = self.point_3, end = self.point_1)

    self.v1 = [self.point_2.x - self.point_1.x, self.point_2.y - self.point_1.y]
    self.v1_inv = [self.point_1.x - self.point_2.x, self.point_1.y - self.point_2.y]
    self.v2 = [self.point_3.x - self.point_2.x, self.point_3.y - self.point_2.y]
    self.v2_inv = [(self.point_2.x - self.point_3.x)*-1, self.point_2.y - self.point_3.y]    
    self.v3 = [self.point_3.x - self.point_1.x, self.point_3.y - self.point_1.y]
    self.v3_inv = [(self.point_1.x - self.point_3.x)*-1, self.point_1.y - self.point_3.y]    
    self.angles = self.compute_inner_angles()
    self.sides_lenght = self.auxiliar_width()

  def vertices(self) -> list[Point]:
    return [self.point_1, self.point_2, self.point_3]
      
  def vertices_repr(self) -> list[Point]:
    list_vertices = ["This are the vertices of the Triangle",
                      f"Point 1: {self.point_1}", 
                      f"Point 2: {self.point_2}",
                      f"Point 3: {self.point_3}"]
    return list_vertices

  def edges_repr(self) -> list[Line]:
    list_edges = ["These are the sides of the Triangle",
                  f"Edge 1: {self.edge_1}", 
                  f"Edge 2: {self.edge_2}",
                  f"Edge 3: {self.edge_3}"]
    return list_edges  

  def auxiliar_width(self) -> list[float]:
    va = [self.point_2.x - self.point_1.x, self.point_2.y - self.point_1.y]
    vb = [self.point_3.x - self.point_2.x, self.point_3.y - self.point_2.y]
    vc = [self.point_3.x - self.point_1.x, self.point_3.y - self.point_1.y]
    hip1 = ((va[0]**2)+(va[1]**2))**0.5
    hip2 = ((vb[0]**2)+(vb[1]**2))**0.5
    hip3 = ((vc[0]**2)+(vc[1]**2))**0.5
    return (hip1, hip2, hip3)
    
  def compute_perimeter(self) -> float:
    s = 0
    for i in self.auxiliar_width():
      s += i
    return s
    
  def compute_perimeter_repr(self) -> list:
    return ["Perimeter of Triangle: "] + [self.compute_perimeter()]
  
  def compute_area(self) -> float:
    s = self.compute_perimeter()/2
    a = self.sides_lenght[0]
    b = self.sides_lenght[1]
    c = self.sides_lenght[2]
    return round((s*(s-a)*(s-b)*(s-c))**0.5, 5)
    
  def compute_area_repr(self) -> list:
    return ["Area of Triangle: "] + [self.compute_area()]
    
  def compute_inner_angles(self) -> list[float]:
    # This is for help to remember the vectors
    # self.v1 = [self.point_2.x - self.point_1.x, self.point_2.y - self.point_1.y]
    # self.v1_inv = [self.point_1.x - self.point_2.x, self.point_1.y - self.point_2.y]
    # self.v2 = [self.point_3.x - self.point_2.x, self.point_3.y - self.point_2.y]
    # self.v3 = [self.point_3.x - self.point_1.x, self.point_3.y - self.point_1.y]

    point_product_1 = self.v1[0]*self.v3[0] + self.v1[1]*self.v3[1]
    point_product_2 = self.v1_inv[0]*self.v2[0] + self.v1_inv[1]*self.v2[1]

    hip_1 = ((self.v1[0]**2)+(self.v1[1]**2))**0.5
    hip_2 = ((self.v2[0]**2)+(self.v2[1]**2))**0.5
    hip_3 = ((self.v3[0]**2)+(self.v3[1]**2))**0.5        

    degree_1 = point_product_1/(hip_1*hip_3)
    degree_2 = point_product_2/(hip_1*hip_2)

    angle_1 = round(degrees(acos(degree_1)), 1)
    angle_2 = round(degrees(acos(degree_2)), 1)
    angle_3 = round(180 -(angle_1 + angle_2), 1)
    return [angle_1,angle_2,angle_3]

  def inner_angles(self) -> list[float]:
    return ["Inner Angles of Triangle"] + self.angles

  def __repr__(self) -> str:
    repr = (self.vertices_repr() + self.edges_repr() + self.inner_angles() 
            + self.compute_area_repr() + self.compute_perimeter_repr())
    for i in repr:
      print(i)
    return "That is all i got"

class Isoceles(Triangle):
  def __init__(self, width: float, height: float, left_point: "Point"):
    self.width = width
    self.height = height
    self.left_point = left_point
    super().__init__(point_1 = left_point,
                     point_2 = Point((left_point.x + width)/2, left_point.y + height),
                     point_3 = Point(left_point.x + width, left_point.x)) 
    pass

class Equilateral(Triangle):
  def __init__(self, width: float, left_point: "Point"):
    self.width = width
    self.left_point = left_point

    height = (((3)**0.5/2)) * width

    point_1 = left_point
    point_2 = Point(left_point.x + width, left_point.y)
    point_3 = Point(left_point.x + width/2, left_point.y + height)

    super().__init__(point_1=point_1, point_2=point_2, point_3=point_3)

class Scalene(Triangle):
  def __init__(self, point_1: "Point", point_2: "Point", point_3: "Point"):
    super().__init__(point_1 = point_1, point_2 = point_2, point_3 = point_3)
    self.side_1 = round(self.sides_lenght[0], 5)
    self.side_2 = round(self.sides_lenght[1], 5)  
    self.side_3 = round(self.sides_lenght[2], 5)
    
    if (self.side_1 == self.side_2) or (self.side_1 == self.side_3) or (self.side_2 == self.side_3):
      raise ValueError("This is NOT an scalene triangle, try again")

class TriRectangle(Triangle):
  def __init__(self, left_point: "Point", width: float, height: float):
    point_1 = left_point
    point_2 = Point(point_1.x + width, point_1.y)
    point_3 = Point(point_1.x, point_1.y + height)
    super().__init__(point_1 = point_1, point_2 = point_2, point_3 = point_3)
    
#Pruebas JoJo
data_1 = TriRectangle(left_point = Point(0,0), width = 10, height = 5)
print(data_1.__repr__())
