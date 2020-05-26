from msp import msp, simtools
import time
import math
import numpy as np

DATAFILE = "runs/Aerobraking.csv"
ATMOSPHEREDATA = "densityModels/MarsDensity.csv"
SPEED = 1000  # __ times speed
RUNTIME = 300000
print("Total runtime will be:", RUNTIME, "s or:", RUNTIME/3600, "hours or:", RUNTIME/86400, "days")

# USE km AS STANDARD DISTANCE UNIT
# USE s AS STANDARD TIME UNIT
AU = 149.6e6  # km
muSun = 1.327178e11
currentTime = time.time()
limitAltitude = 200 # 260  #[km]. At this altitude density is just below 1*10^-10


MarsAtmosphere=msp.Atmosphere(limitAltitude, densityFile=ATMOSPHEREDATA)
Mars = msp.Planet(4.282837e4, 3396.2, 1.52367934 * AU, muSun, MarsAtmosphere)

r = np.array([21508.114845629447, 0.0, 982.3450283462487])
v = np.array([-2.968111925169866, 0.0, -1.4808260236254678])

# CD is increased times 50 here to see the effect.
CD = 1.23 * 100
surfaceArea = 3.6**2 * math.pi

spacecraft = msp.Body(Mars, 3000, CD, surfaceArea )
spacecraft.initPositionOrbit(r,v)

# PROPAGATE Here
dt = 1
# These are some precalculated manoeuvres to see the effects
spacecraft.addManoeuvreByDirection(spacecraft.start + 100, -1.332, "t")
spacecraft.addManoeuvreByDirection(spacecraft.start + 8900, -0.3, "t")

rlist = spacecraft.propagate(RUNTIME, DATAFILE, True, dtAtmospheric = dt, dtNormal = dt)

print(np.sqrt(spacecraft.v.dot(spacecraft.v)))
print(spacecraft.e)
print(spacecraft.periapsis)
print("Periaosis alt", spacecraft.periapsis-Mars.r)
print("Apoapsis alt", spacecraft.apoapsis-Mars.r)

simtools.quickAnimate(SPEED,DATAFILE,Mars)