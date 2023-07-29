import math

# predict bullet pathing

def avoidBulletAngle(x,y):
    '''
    Input: Speed on X axis; Speed on Y axis
    Output: Angle perpendicular to bullet angle
    '''
    bulletAngle = math.degrees(math.atan(y/x))
    return bulletAngle+90

def findClosestBullet(objDict, pos):
    for objId in objDict:
        if objDict[objId]["type"] == 2 and pos[0]-50 <= objDict[objId]["position"][0] <= pos[0]+50 and pos[1]-50 <= objDict[objId]["position"][1] <= pos[1]+50:
            return objDict[objId]