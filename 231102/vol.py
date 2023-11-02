import math

def sphVol (Rad):
    vol = (4/3)*math.pi*Rad**3
    return vol

print(sphVol(50))