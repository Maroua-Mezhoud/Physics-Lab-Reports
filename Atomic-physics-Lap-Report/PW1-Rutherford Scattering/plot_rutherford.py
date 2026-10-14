
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# 1. Read the simulation data
# --------------------------------------------------
data = pd.read_csv("data.csv")

b = data["Impact_Parameter_b_fm"].to_numpy()
theta_sim = data["Diffusion_Theta_Degrees"].to_numpy()

# --------------------------------------------------
# 2. Define the theoretical Rutherford scattering law
# Z = 79, Ec = 6 MeV, k*e^2 = 1.44 MeV.fm
# --------------------------------------------------
Z = 79
Ec = 6.0
ke2 = 1.44

def theta_theory(b):
    return np.degrees(
        2 * np.arctan((ke2 * Z) / (Ec * b))
    )

# Split the curve at b = 0 to avoid division by zero
b_negative = np.linspace(-70, -0.5, 1000)
b_positive = np.linspace(0.5, 70, 1000)

# --------------------------------------------------
# 3. Plot simulation points and theoretical curves
# --------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

ax.scatter(
    b, theta_sim,
    s=28,
    alpha=0.8,
    label="Simulation data",
    zorder=3
)

line, = ax.plot(
    b_negative,
    theta_theory(b_negative),
    linewidth=2,
    label="Theoretical curve"
)

ax.plot(
    b_positive,
    theta_theory(b_positive),
    linewidth=2,
    color=line.get_color()
)

ax.set_xlabel(r"Impact parameter $b$ (fm)", fontsize=12)
ax.set_ylabel(r"Scattering angle $\theta$ (degrees)", fontsize=12)

ax.set_title("Rutherford Scattering: Simulation vs Theory")
ax.set_xlim(-70, 70)
ax.set_ylim(-190, 190)

ax.axhline(0, color="black", linewidth=0.7)
ax.grid(True, alpha=0.25)
ax.legend()
fig.tight_layout()

# --------------------------------------------------
# 4. Save the figures
# --------------------------------------------------
output_dir = Path("figures")
output_dir.mkdir(exist_ok=True)

fig.savefig(
    output_dir / "rutherford_scattering.png",
    dpi=300,
    bbox_inches="tight"
)

fig.savefig(
    output_dir / "rutherford_scattering.pdf",
    bbox_inches="tight"
)

print(f"Number of simulation points: {len(data)}")
print("Figures saved successfully in the figures folder.")

plt.show()
