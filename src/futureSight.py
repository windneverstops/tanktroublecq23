import math
import random
from operator import add
from intersect import doIntersect, Point
from shootingAlgorithm import checkLOS

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

def findIncomingBullet(objDict, pos):
    for objId in objDict:
        if objDict[objId]["type"] == 2 and checkLOS(objDict[objId]["position"], pos, objDict):
            bullet = objDict[objId]
            # m = bullet["velocity"][1] / bullet["velocity"][0]
            # c = bullet["position"][1] - m*bullet["position"][0]
            r1 = Point(pos[0]-15, pos[1]+15)
            r2 = Point(pos[0]+15, pos[1]+15)
            r3 = Point(pos[0]-15, pos[1]-15)
            r4 = Point(pos[0]+15, pos[1]-15)
            p2 = Point(*bullet["position"])
            # qx = pos[0]+(100*math.copysign(pos[0]-bullet["position"][0]))
            # qy = m*qx + c
            q2 = Point(*list(map(add, bullet["position"], bullet["velocity"])))
            for side in [[r1, r2], [r2, r3], [r3, r4], [r4, r1]]:
                p1 = side[0]
                q1 = side[1]
                
                if doIntersect(p1, q1, p2, q2):
                    return bullet

