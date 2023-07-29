import math
from operator import add
from intersect import doIntersect, Point
"""
1. Consider defensive shooting
2. Predictive shooting
    - Follow trend, etc

"""

def shootIncomingBullet() -> int:
    pass

def enemyCurrentAngle(enemy, pos):
    if not enemy["position"][0]-pos[0]:
        return 270 if enemy["position"][1] < pos[1] else 90
    m = (enemy["position"][1]-pos[1]) / (enemy["position"][0]-pos[0])
    res = math.degrees(math.atan(m))
    if enemy["position"][0] < pos[0]:
        res += 180
    return res

def enemyPredictAngle(enemy, pos):
    bulletSpeed = 450 # TODO - replace this value with an arg, bullet vel can change based on powerup
    t = 0.25
    while True:
        prediction = list(map(add, enemy["position"], [x*t for x in enemy["velocity"]]))
        if math.dist(pos, prediction) <= bulletSpeed*t:
            break
        t += 0.25
    if not prediction[0]-pos[0]:
        return 270 if prediction[1]-pos[1] else 90
    m = (prediction[1]-pos[1]) / (prediction[0]-pos[0])
    res = math.degrees(math.atan(m))
    if prediction[0] < pos[0]:
        res += 180
    return res

def checkEnemyLOS(enemy, pos, objDict):
    p2 = Point(*pos)
    q2 = Point(*enemy["position"])
    for objId in objDict:
        if (objDict[objId]["type"] == 3 or objDict[objId]["type"] == 4):
            wallPos = objDict[objId]["position"]
            r1 = Point(wallPos[0]-9, wallPos[1]+9)
            r2 = Point(wallPos[0]+9, wallPos[1]+9)
            r3 = Point(wallPos[0]-9, wallPos[1]-9)
            r4 = Point(wallPos[0]+9, wallPos[1]-9)
            for side in [[r1, r2], [r2, r3], [r3, r4], [r4, r1]]:
                p1 = side[0]
                q1 = side[1]
                
                if doIntersect(p1, q1, p2, q2):
                    return False
    return True