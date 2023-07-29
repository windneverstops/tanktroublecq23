import math
import numpy as np
from operator import add
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