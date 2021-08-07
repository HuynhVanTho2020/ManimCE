from manim import *
import math

# --- 1. Hàm lấy giao điểm của hai Line.
# --- 2. Trực trực tâm của tam giác
# --- 3. Trọng tâm của 3 điểm    
# --- 4. Tâm đường tròn ngoại tiếp tam giác
# --- 5. Bán kính đường tròn ngoại tiếp tam giác
# --- 6. Tâm đường tròn nội tiếp
# --- 7. Bán kính đường tròn nội tiếp
# --- 8. Tâm đường tròn bàn tiếp - 3 tâm
# --- 9. Bán kính đường tròn bàn tiếp - 3 bán kính    
# --- 10. Hình chiếu 1 đỉnh lên cạnh của tam giác

# -----------1
"""
get_intersect function calculates the intersect position of two lines
when two lines are paralleled to each other
it will return `parallel` parameter
For example: 
dot = Dot()
dot.add_updater(lambda m: m.move_to(get_intersect(line1, line2, LEFT * 100))
""" 

def get_intersect(line1, line2, parallel=1):
    p1, p2 = line1.get_start_and_end()
    p3, p4 = line2.get_start_and_end()

    # Line1 is a1*x+b1*y=c1
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    # Line2 is a2*x+b2*y=c2
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return parallel
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x * RIGHT + y * UP    
def get_intersect(line1, line2, parallel=1):
    p1, p2 = line1.get_start_and_end()
    p3, p4 = line2.get_start_and_end()

    # Line1 is a1*x+b1*y=c1
    a1 = p2[1] - p1[1]
    b1 = p1[0] - p2[0]
    c1 = a1 * p1[0] + b1 * p1[1]

    # Line2 is a2*x+b2*y=c2
    a2 = p4[1] - p3[1]
    b2 = p3[0] - p4[0]
    c2 = a2 * p3[0] + b2 * p3[1]

    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return parallel
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x * RIGHT + y * UP

# --- 2. Trực trực tâm của tam giác
def get_orthocenter(A, B, C):
    a = Line(B,C).get_length()
    b = Line(C,A).get_length()
    c = Line(A,B).get_length()
    
    AngleA = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    AngleB = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    AngleC = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    Cx, Cy = C[0], C[1]

    xup = a / math.cos(AngleA) * Ax + b / math.cos(AngleB) * Bx + c / math.cos(AngleC) * Cx
    yup = a / math.cos(AngleA) * Ay + b / math.cos(AngleB) * By + c/ math.cos(AngleC) * Cy
    down = a / math.cos(AngleA) + b / math.cos(AngleB) + c / math.cos(AngleC)
    return np.array([xup/down,yup/down,0])  

# --- 3. Trọng tâm của 3 điểm    
def get_centroid(A, B, C): 
    # A, B, C = Polygon.get_vertices(self)
    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    Cx, Cy = C[0], C[1]
    return np.array([(Ax + Bx + Cx) / 3, (Ay + By + Cy) / 3, 0])      

# --- 4. Tâm đường tròn ngoại tiếp tam giác
def get_circumcenter(A, B, C):
    a = Line(B,C).get_length()
    b = Line(C,A).get_length()
    c = Line(A,B).get_length()
    
    AngleA = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    AngleB = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    AngleC = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    Cx, Cy = C[0], C[1]

    xup = Ax * math.sin(2 * AngleA) + Bx * math.sin(2 * AngleB) + Cx * math.sin(2 * AngleC)
    yup = Ay * math.sin(2 * AngleA) + By * math.sin(2 * AngleB) + Cy * math.sin(2 * AngleC)
    down = math.sin(2 * AngleA) + math.sin(2 * AngleB) + math.sin(2 * AngleC) 
    return np.array([xup/down, yup/down, 0])  

# --- 5. Bán kính đường tròn ngoại tiếp tam giác
def get_circumcenter_radius(A, B, C):
    a = Line(B,C).get_length()
    b = Line(C,A).get_length()
    c = Line(A,B).get_length()
    
    AngleA = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    AngleB = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    AngleC = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    Cx, Cy = C[0], C[1]

    xup = Ax * math.sin(2 * AngleA) + Bx * math.sin(2 * AngleB) + Cx * math.sin(2 * AngleC)
    yup = Ay * math.sin(2 * AngleA) + By * math.sin(2 * AngleB) + Cy * math.sin(2 * AngleC)
    down = math.sin(2 * AngleA) + math.sin(2 * AngleB) + math.sin(2 * AngleC) 
    I = np.array([xup/down, yup/down, 0])
    return math.sqrt((I[0]-Ax)**2 +(I[1]-Ay)**2)       

# --- 6. Tâm đường tròn nội tiếp
def get_incenter(A, B, C): 
    a = Line(B,C).get_length()
    b = Line(C,A).get_length()
    c = Line(A,B).get_length()

    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    Cx, Cy = C[0], C[1]

    x = (a * Ax + b * Bx + c * Cx) / (a + b + c)
    y = (a * Ay + b * By + c * Cy) / (a + b + c)

    return np.array([x, y, 0])

# --- 7. Bán kính đường tròn nội tiếp
def get_incircle_radius(A, B, C):
    a = Line(B,C).get_length()
    b = Line(C,A).get_length()
    c = Line(A,B).get_length()
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S*2/(a+b+c)   

# --- 8. Tâm đường tròn bàn tiếp - 3 tâm
def get_excenter(A, B, C):
    # A, B, C = Polygon.get_vertices(self)
    # a, b, c = self.get_side_length()
    a = Line(B,C).get_length()
    b = Line(C,A).get_length()
    c = Line(A,B).get_length()

    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    Cx, Cy = C[0], C[1]

    Ja_x = (-a * Ax + b * Bx + c * Cx) / (-a + b + c)
    Ja_y = (-a * Ay + b * By + c * Cy) / (-a + b + c)
    Jb_x = (a * Ax - b * Bx + c * Cx) / (a - b + c)
    Jb_y = (a * Ay - b * By + c * Cy) / (a - b + c)
    Jc_x = (a * Ax + b * Bx - c * Cx) / (a + b - c)
    Jc_y = (a * Ay + b * By - c * Cy) / (a + b - c)

    return np.array([Ja_x, Ja_y, 0]), np.array([Jb_x, Jb_y, 0]), np.array([Jc_x, Jc_y, 0])    

# --- 9. Bán kính đường tròn bàn tiếp - 3 bán kính    
def get_excircle_radius(A, B, C):
    a = Line(B,C).get_length()
    b = Line(C,A).get_length()
    c = Line(A,B).get_length()
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))

    return 2*S/(-a+b+c), 2*S/(a-b+c), 2*S/(a+b-c)

# --- 10. Hình chiếu 1 đỉnh lên cạnh của tam giác: Ha là hình chiếu lên BC,
def get_point_project(A, B, C):
    # A, B, C = Polygon.get_vertices(self)
    H = get_orthocenter(A, B, C)
    Ha = get_intersect(Line(A,H), Line(B,C)) # hình chiếu  của A lên BC
    Hb = get_intersect(Line(B,H), Line(A,C)) # hình chiếu của B lên CA
    Hc = get_intersect(Line(C,H), Line(A,B)) # hình chiếu của C lên AB
    return [Ha, Hb, Hc]    
