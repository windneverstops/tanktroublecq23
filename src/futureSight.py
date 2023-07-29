import math

# predict bullet pathing

def avoidBulletAngle(x,y):
    '''
    Input: Speed on X axis; Speed on Y axis
    Output: Angle perpendicular to bullet angle
    '''

    bulletAngle = math.atan(y/x)
    return bulletAngle+90

def findClosestBullet(objDict, pos):
    for obj in objDict:
        if obj.type == "2" and pos[0]-20 <= obj.position[0] <= pos[0]+20 and pos[1]-20 <= obj.position[1] <= pos[1]+20:
            return obj