from operator import add
from shootingAlgorithm import checkLOS
import math

def pathfind(enemy, pos, objDict, center):
    enemyDist = math.dist(enemy["position"], pos)
    for objId in objDict:
        obj = objDict[objId]
        # Avoid Boundary
        if obj["type"] == 6:
            if (obj["position"][0][0] >= pos[0]-100 or obj["position"][1][1] >= pos[1]-100 or obj["position"][2][0] <= pos[0]+100 or obj["position"][3][1] <= pos[1]+100):
                return "path", center
    if enemyDist >= 300 and not checkLOS(enemy["position"], pos, objDict):
        return "path", enemy["position"]
    return "move", -1
        