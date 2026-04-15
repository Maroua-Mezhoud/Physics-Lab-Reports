# 🌡️ Thermodynamics Laboratory: Thermal Conductivity Analysis

This repository contains a laboratory report on **Thermal Conductivity in Construction Materials**, developed as part of the undergraduate Thermodynamics curriculum. The work combines classical experimental methods with numerical modeling techniques to support data analysis and interpretation.

---

## 🎓 Academic Context

- **University:** Mohamed El Bachir El Ibrahimi University of Bordj Bou Arréridj  
- **Faculty:** Faculty of Science and Technology  
- **Department:** Department of Materials Science  
- **Laboratory No.:** 13  
- **Course:** Thermodynamics (Year 2)  
- **Supervision:** Under the academic guidance of **Dr. N. Benchiheub**

---

## 📂 Featured Experiment: Thermal Conductivity of Construction Materials (PW4)

- **Focus:** Analysis of heat transfer in construction materials (Wood, Fermacell, and Rohacell) using the guarded plate method with the Cassy measurement system.  
- **Methodology:** Estimation of thermal conductivity ($\lambda$) based on electrical power input and measured temperature differences ($\Delta T$) across samples under steady-state conditions.  
- **Computational Component:** A Python-based numerical model was developed to reconstruct and analyze transient temperature evolution, supporting interpretation in accordance with Fourier’s law of heat conduction.  
- **Key Outcome:** Rohacell exhibited the lowest thermal conductivity among the tested materials, consistent with its performance as an effective thermal insulator and in agreement with reported literature values.

---

## 🛠️ Technical Implementation

- **LaTeX Typesetting:** Structured using advanced packages such as `tcolorbox` and `listings` to ensure clear scientific presentation and proper documentation of code and results.  
- **Python Simulation:** Implemented using `NumPy` and `Matplotlib` to model transient thermal behavior using an exponential approach-to-equilibrium function:  
  $T(t) = A - B e^{-t/C}$  
- **Data Visualization:** Time-series analysis includes asymptotic convergence behavior and stochastic noise to represent experimental measurement uncertainty.

---

## ⚖️ Usage and Academic Integrity

- **Purpose:** This repository is intended for educational and academic reference. It documents experimental methodology, data analysis procedures, and computational modeling approaches.  
- **Reproducibility:** All code and figures are provided to support transparency and reproducibility of the results.  
- **Academic Use:** Proper attribution is expected when referencing this work in academic or educational contexts.

---

**Academic Year:** 2025–2026  
**Author:** Maroua Mezhoud
