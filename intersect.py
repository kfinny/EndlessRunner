class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self) -> tuple:
        return self.x, self.y

    def __str__(self) -> str:
        return f'x={self.x}, y={self.y}'

class LineSegment:

    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1,y1)
        self.p2 = Point(x2, y2)

    def __str__(self) -> str:
        return f'p1=({self.p1}), p2=({self.p2})'


def ccw(A: Point, B: Point, C: Point) -> bool:
    """Check if points A, B, and C are in a counterclockwise order."""
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


def intersect(A: Point, B: Point, C: Point, D: Point) -> bool:
    """Check if line segment AB intersects line segment CD."""
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def test_intersection1(segment1: LineSegment, segment2: LineSegment) -> bool:
    """Test whether two line segments intersect."""
    A, B = (segment1.p1, segment1.p2)
    C, D = (segment2.p1, segment2.p2)
    return intersect(A, B, C, D)


def test_intersection(segment1: LineSegment, segment2: LineSegment) -> bool:
    """Check if two lines defined by points intersect."""
    x1, y1 = segment1.p1.coordinates()
    x2, y2 = segment1.p2.coordinates()
    x3, y3 = segment2.p1.coordinates()
    x4, y4 = segment2.p2.coordinates()
    
    denominator = ((y4 - y3) * (x2 - x1)) - ((x4 - x3) * (y2 - y1))
    if denominator == 0:
        return False  # Lines are parallel
    
    ua = (((x4 - x3) * (y1 - y3)) - ((y4 - y3) * (x1 - x3))) / denominator
    ub = (((x2 - x1) * (y1 - y3)) - ((y2 - y1) * (x1 - x3))) / denominator
    
    if 0 <= ua <= 1 and 0 <= ub <= 1:
        # Intersection point lies within the line segments
        # return True, Point(x1 + ua * (x2 - x1), y1 + ua * (y2 - y1))
        return True
    
    return False

def test_code():
    point = None
    # Example usage:
    segment1 = LineSegment(1, 1, 4, 4)
    segment2 = LineSegment(1, 4, 4, 1)
    print(test_intersection1(segment1, segment2))  # Should return True (intersection)
    check = test_intersection(segment1, segment2)
    print(f'({check}, {point})')

    segment1 = LineSegment(1, 1, 4, 4)
    segment2 = LineSegment(5, 1, 5, 5)
    print(test_intersection1(segment1, segment2))
    check = test_intersection(segment1, segment2)
    print(f'({check}, {point})')

    segment1 = LineSegment(0, 0, 4, 4)
    segment2 = LineSegment(1, 1, 5, 5)
    print(test_intersection1(segment1, segment2))
    check = test_intersection(segment1, segment2)
    print(f'({check}, {point})')
