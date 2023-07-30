from operator import add
import numpy as np

def pathfind(enemy, pos, objDict, center):
    for objId in objDict:
        obj = objDict[objId]
        # Avoid Boundary
        if obj["type"] == 6:
            if (obj["position"][0][0] >= pos[0]-100 or obj["position"][1][1] >= pos[1]-100 or obj["position"][2][0] <= pos[0]+100 or obj["position"][3][1] <= pos[1]+100):
                return "path", center
    return "move", -1
        