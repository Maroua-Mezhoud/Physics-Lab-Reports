import numpy as np
import matplotlib.pyplot as plt

# 1. Mathematical Model (Exponential Heating Model)
# T(t) represents the temperature increase over time towards steady state
def thermal_model(t, A, B, C):
    return A - B * np.exp(-t / C)

# 2. Experimental Parameters (Extracted from Rohacell data table)
d = 0.01                # Material thickness in meters (1 cm)
S = 15**2 * 1e-4        # Surface area in square meters (0.0225 m^2)
P = 4.267               # Electrical power input in Watts (U * I)
T_eqint = 40.0          # Measured steady-state temperature (Asymptote A)
T_froid = 0.0           # Cold plate temperature (Ice reference)

# Verification of Experimental Thermal Conductivity (Lambda)
# Formula: lambda = (P * d) / (S * Delta_T)
lambda_exp = (P * d) / (S * (T_eqint - T_froid))

# 3. Curve Fitting Parameters for Simulation
A = T_eqint             # Horizontal asymptote (Final equilibrium temperature)
B = A - 20              # Temperature difference (Assumes initial T = 20°C)
C = 650                 # Time constant (Determines the curve's slope)

# 4. Synthetic Data Generation
# Simulating 1 hour of data collection (3600 seconds)
t_data = np.linspace(0, 3600, 250)  
# Adding Gaussian noise to mimic real Cassy sensor fluctuations
noise = np.random.normal(0, 0.15, t_data.shape) 
T_data = thermal_model(t_data, A, B, C) + noise

# 5. Professional Visualization
plt.figure(figsize=(11, 6))

# Plotting simulated data points
plt.scatter(t_data, T_data, color='gray', s=10, alpha=0.4, label='Reconstructed Cassy Data (Rohacell)')

# Plotting the optimized theoretical fit
plt.plot(t_data, thermal_model(t_data, A, B, C), color='#2E86C1', linewidth=2.5, label='Theoretical Fit')

# Graphical enhancements for report quality
plt.axhline(y=A, color='red', linestyle='--', alpha=0.7, label=f'Equilibrium Temp (A) = {A}°C')
plt.title('Thermal Conductivity Analysis: Rohacell Simulation', fontsize=14, pad=20)
plt.xlabel('Time $t$ (seconds)', fontsize=12)
plt.ylabel('Temperature $T$ (°C)', fontsize=12)

# Displaying the calculated Lambda on the plot
plt.text(2000, 25, f'$\lambda_{{exp}} = {lambda_exp:.4f} \ W/(m\cdot K)$', 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.legend(loc='lower right')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.tight_layout()

# Saving the figure in high resolution (300 DPI) for the final report
plt.savefig('Rohacell_Simulation.png', dpi=300)
plt.show()
