import math
import random
from operator import add

# predict bullet pathing

def avoidBulletAngle(x,y):
    """
    Input: Speed on X axis; Speed on Y axis
    Output: Angle perpendicular to bullet angle
    """
    if not x:
        bulletAngle = 90 if y > 0 else 270
    else:
        bulletAngle = math.degrees(math.atan(y/x))
    return bulletAngle+(90*random.choice([-1, 1]))

# def findClosestBullet(objDict, pos):
#     closest = None
#     dist = 130
#     for objId in objDict:
#         obj = objDict[objId]
#         if obj["type"] == 2 and math.dist(obj["position"], pos) < dist:
#             closest = obj
#             dist = math.dist(obj["position"], pos)
#     return closest
    
# A Python3 program to find if 2 given line segments intersect or not
  
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
# Given three collinear points p, q, r, the function checks if 
# point q lies on line segment 'pr' 
def onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False
  
def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
      
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/ 
    # for details of below formula. 
      
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
          
        # Clockwise orientation
        return 1
    elif (val < 0):
          
        # Counterclockwise orientation
        return 2
    else:
          
        # Collinear orientation
        return 0
  
# The main function that returns true if 
# the line segment 'p1q1' and 'p2q2' intersect.
def doIntersect(p1,q1,p2,q2):
      
    # Find the 4 orientations required for 
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
  
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True
  
    # Special Cases
  
    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
  
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
  
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
  
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
  
    # If none of the cases
    return False
# This code is contributed by Ansh Riyal
# From https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

def findIncomingBullet(objDict, pos):
    for objId in objDict:
        if objDict[objId]["type"] == 2 and checkLOS(objDict[objId]["position"], pos, objDict):
            bullet = objDict[objId]
            # m = bullet["velocity"][1] / bullet["velocity"][0]
            # c = bullet["position"][1] - m*bullet["position"][0]
            r1 = Point(pos[0]-10, pos[1]+10)
            r2 = Point(pos[0]+10, pos[1]+10)
            r3 = Point(pos[0]-10, pos[1]-10)
            r4 = Point(pos[0]+10, pos[1]-10)
            p2 = Point(*bullet["position"])
            # qx = pos[0]+(100*math.copysign(pos[0]-bullet["position"][0]))
            # qy = m*qx + c
            q2 = Point(*list(map(add, bullet["position"], bullet["velocity"])))
            for side in [[r1, r2], [r2, r3], [r3, r4], [r4, r1]]:
                p1 = side[0]
                q1 = side[1]
                
                if doIntersect(p1, q1, p2, q2):
                    return bullet

