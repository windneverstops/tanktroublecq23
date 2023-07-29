import math
import sys
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
    return math.degrees(math.atan(m))

def enemyPredictAngle(enemy, pos):
    prediction = list(map(add, enemy["position"], enemy["velocity"]))
    if not prediction[0]-pos[0]:
        return 270 if prediction[1]-pos[1] else 90
    m = (prediction[1]-pos[1]) / (prediction[0]-pos[0])
    return math.degrees(math.atan(m))