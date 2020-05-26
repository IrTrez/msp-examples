from msp import msp, simtools
import time
import math
import numpy as np

DATAFILE = "runs/ManouvreTest.csv" # saves csv data here
SPEED = 700  # __ times speed for the animation

# USE km AS STANDARD DISTANCE UNIT
# USE s AS STANDARD TIME UNIT

currentTime = time.time()
Earth = simtools.Earth

# Angles here are given in degrees
a = 10000
e = 0.3
i = 1
Omega = 0.0
omega = 60.0
trueAnomaly = 40

CD = 1.2
surfaceArea = 3.6**2 * math.pi
mass = 100

spacecraft = msp.Body(Earth, mass, CD, surfaceArea )
# Normally initKeplerOrbit takes radians but setting the useDegrees parameter true\
# Allows for the use of degrees
spacecraft.initKeplerOrbit(a,e,i,Omega,omega,trueAnomaly, useDegrees=True)

# Add manoeuvers before propagate
# Example of an inclination change
# Note that for best results add Manoeuvres in order.
spacecraft.addManoeuvreByDirection("p0", 1.3, "t")
spacecraft.addManoeuvreByDirection("p2", -1.3, "t")
spacecraft.addManoeuvreByDirection("a1", 0.3, "n")
spacecraft.addManoeuvreByDirection("a2", 0.3, "n")

# Some more examples of manoeuvres
# spacecraft.addManoeuvreByDirection(1000, -0.5, "n")
# spacecraft.addManoeuvreByDirection(spacecraft.start + 1 * spacecraft.orbitalPeriod, 6, "n")
# spacecraft.addManoeuvreByDirection("p1", 1, "r")\
# spacecraft.addManoeuvreByVector(spacecraft.start + 1000, np.array([1,-1,1]))

# PROPAGATE This actually runs the simulation, In this case it is not atmospheric
spacecraft.propagate(12*spacecraft.orbitalPeriod, DATAFILE, False)

# Fast form of animate that doesn't save.
simtools.quickAnimate(SPEED, DATAFILE, Earth)
