import math

# predict bullet pathing

def avoidBulletAngle(x,y):
    """
    Input: Speed on X axis; Speed on Y axis
    Output: Angle perpendicular to bullet angle
    """
    bulletAngle = math.degrees(math.atan(y/x))
    return bulletAngle+90

def findClosestBullet(objDict, pos):
    closest = None
    dist = 9999999
    for objId in objDict:
        obj = objDict[objId]
        if obj["type"] == 2 and math.dist(obj["position"], pos) < dist:
            closest = obj
            dist = math.dist(obj["position"], pos)
    return closest
    
        
def findIncomingBullets(objDict, pos):
    for objId in objDict:
        if objDict[objId]["type"] == 2:
            bullet = objDict[objId]
            m = bullet["velocity"][0] / bullet["velocity"][1]
            c = bullet["position"][1] - m*bullet["position"][0]

