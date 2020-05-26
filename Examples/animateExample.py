from msp import animator, simtools

# Run Manoeuvre.py for data and install FFMPEG before trying this.
# FFMPEG can be installed via chocolaty or via the guide on the MSP github
SPEED = 500
DATAFILE = "runs/ManouvreTest.csv"
Mars = simtools.Mars

animator.animate(SPEED, DATAFILE, Mars, "orange")