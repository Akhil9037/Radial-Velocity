from numpy import*
from  matplotlib.pyplot import*

# Constants and Given Parameters
i = np.radians(60)       # Inclination to radians
a_star_au = 0.05         # Semi-major axis in AU
P_years = 5              # Period in years
AU_to_km = 1.496e8       # conversion factor
year_to_sec = 3.154e7    # conversion factor

# Calculate K (Semi-amplitude) for a circular orbit as a baseline
# K = (2 * pi * a * sin(i)) / (P * sqrt(1 - e^2))
def calculate_K(e):
    return (2 * pi * a_star_au * AU_to_km * sin(i)) / (P_years * year_to_sec * sqrt(1 - e**2))

# Orbital phase (theta) from 0 to 720 degrees
theta_deg = linspace(0, 720, 1000)
theta_rad = radians(theta_deg)

omegas = [0, 30, 60, 90]
eccentricities = [0.0, 0.7]



for e in eccentricities:
    # 1. Start a brand new, separate window for this eccentricity
    figure() 
    
    K = calculate_K(e)

    for w_deg in omegas:
        w_rad = radians(w_deg)
     
        vr = K * (cos(w_rad + theta_rad) + e * cos(w_rad))
        
        # 2. Plot on the current active figure
        plot(theta_deg, vr, label=f'$\omega = {w_deg}^\circ$')

    # Add labels and legend to this specific figure 
    title(f'Synthetic Radial Velocity Curves (e = {e})')
    xlabel('Orbital phase $\\theta$ (degrees)')
    ylabel('Radial velocity $v_r$ (km/s)')
    legend()
    grid(True)

# 4. Display all windows at once
show()

    
    
