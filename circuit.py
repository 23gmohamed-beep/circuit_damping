import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 1. CIRCUIT MODEL (SERIES RLC SYSTEM)
# ==========================================

# Source voltage (step input initial energy source)
Vs = 12.0

# Resistor used only to define initial current condition (not in all states)
R_bottom = 100.0

# Inductor and capacitor define oscillation dynamics
L = 1.0          # inductance in Henry
C = 15e-6        # capacitance in Farads

# ------------------------------------------
# INITIAL CONDITIONS (energy stored system)
# ------------------------------------------

# Initial current comes from Ohm's law at switching moment:
# i(0) = Vs / R
i0 = Vs / R_bottom

# Capacitor voltage cannot change instantly:
# v_C(0) = 0 (assumed uncharged)
v0 = 0.0

# From capacitor law:
# i = C dv/dt  →  dv/dt = i/C
dv0 = i0 / C

# ------------------------------------------
# TIME DOMAIN SIMULATION
# ------------------------------------------

# Time vector for transient response
t = np.linspace(0, 0.15, 5000)

# Natural angular frequency of LC system:
# ω₀ = 1 / √(LC)
omega_0 = 1.0 / np.sqrt(L * C)

# Critical resistance separating damping regimes:
# Rc = 2√(L/C)
R_critical = 2 * np.sqrt(L / C)

print(f"Natural Frequency ω₀ = {omega_0:.2f} rad/s")
print(f"Critical Resistance Rc = {R_critical:.2f} Ω")

# ==========================================
# 2. UNDAMPED CASE (R = 0)
# ==========================================

# Governing equation reduces to pure LC oscillator:
# d²v/dt² + ω₀² v = 0

# General solution:
# v(t) = A sin(ω₀ t) + B cos(ω₀ t)

# Applying initial conditions:
# v(0)=0 → B = 0
# dv/dt(0) = dv0 → A = dv0 / ω₀

A2_un = dv0 / omega_0

# Final solution for voltage:
v_un = A2_un * np.sin(omega_0 * t)

# Current obtained from capacitor relation:
# i(t) = C dv/dt
i_un = C * np.gradient(v_un, t, edge_order=2)

# ==========================================
# 3. UNDERDAMPED CASE (R = 10 Ω)
# ==========================================

R_under = 10.0

# Damping factor:
# α = R / (2L)
alpha_under = R_under / (2 * L)

# Damped frequency:
# ω_d = √(ω₀² - α²)
omega_d = np.sqrt(omega_0**2 - alpha_under**2)

# Solution form:
# v(t) = e^(-αt)(A sin(ω_d t) + B cos(ω_d t))

# Initial conditions:
# v(0)=0 → B = 0
# dv/dt(0) → A = dv0 / ω_d

A2_under = dv0 / omega_d

v_under = np.exp(-alpha_under * t) * A2_under * np.sin(omega_d * t)

# Current from derivative of voltage
i_under = C * np.gradient(v_under, t, edge_order=2)

 
# ==========================================
# 4. CRITICALLY DAMPED CASE (R = Rc)
# ==========================================

# Condition: α = ω₀ → repeated root system

alpha_crit = R_critical / (2 * L)

# General solution:
# v(t) = (A + Bt) e^(-αt)

# Initial condition:
# v(0)=0 → A = 0
# dv/dt(0) → B = dv0

v_crit = dv0 * t * np.exp(-alpha_crit * t)

# Current via capacitor relation
i_crit = C * np.gradient(v_crit, t, edge_order=2)

 

# ==========================================
# 5. OVERDAMPED CASE (R = 1000 Ω)
# ==========================================

R_over = 1000.0

# Strong damping factor
alpha_over = R_over / (2 * L)

# Characteristic equation roots:
# s = -α ± √(α² - ω₀²)

s1 = -alpha_over + np.sqrt(alpha_over**2 - omega_0**2)
s2 = -alpha_over - np.sqrt(alpha_over**2 - omega_0**2)

# General solution:
# v(t) = A e^(s1 t) + B e^(s2 t)

# Apply initial conditions:
# v(0)=0 → A + B = 0 → B = -A
# dv/dt(0) = dv0

A1_over = dv0 / (s1 - s2)
A2_over = -A1_over

v_over = A1_over * np.exp(s1 * t) + A2_over * np.exp(s2 * t)

# Current from capacitor law
i_over = C * np.gradient(v_over, t, edge_order=2)

plt.style.use("default")
graph_color = "blue"


# -------------------------------
# FIGURE 1: Remaining Three States
# -------------------------------

states = [ ("Overdamped (1000 Ω)", v_over, i_over),
("Critically Damped (516.4 Ω)", v_crit, i_crit),
("Underdamped (10 Ω)", v_under, i_under),
]

plt.figure(figsize=(14, 12))
plt.suptitle("RLC Circuit Response for Different Resistance Values", fontsize=16)

for idx, (title, voltage, current) in enumerate(states):

    # Voltage subplot
    plt.subplot(3, 2, 2 * idx + 1)
    plt.plot(t * 1000, voltage,
             color=graph_color,
             linewidth=2,
             label=title)
    plt.xlim(0, t[-1] * 1000)   # <-- FIX HERE
    
    plt.xlabel("Time (ms)")
    plt.ylabel("Voltage (V)")
    plt.legend(loc="upper right")
    plt.grid(True)

    # Current subplot
    plt.subplot(3, 2, 2 * idx + 2)
    plt.plot(t * 1000, current,
             color=graph_color,
             linewidth=2,
             label=title)
    plt.xlim(0, t[-1] * 1000)   # <-- FIX HERE

    plt.xlabel("Time (ms)")
    plt.ylabel("Current (A)")
    plt.legend(loc="upper right")
    plt.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()


# -------------------------------
# FIGURE 2: Undamped Alone
# -------------------------------

plt.figure(figsize=(12, 5))
plt.suptitle("Undamped RLC Circuit Response", fontsize=16)

# Voltage
plt.subplot(1, 2, 1)
plt.plot(t * 1000, v_un,
         color=graph_color,
         linewidth=2,
         label="Undamped (0 Ω)")
plt.xlim(0, t[-1] * 1000)   # <-- FIX HERE

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.legend(loc="upper right")
plt.grid(True)

# Current
plt.subplot(1, 2, 2)
plt.plot(t * 1000, i_un,
         color=graph_color,
         linewidth=2,
         label="Undamped (0 Ω)")
plt.xlim(0, t[-1] * 1000)   # <-- FIX HERE

plt.xlabel("Time (ms)")
plt.ylabel("Current (A)")
plt.legend(loc="upper right")
plt.grid(True)

plt.tight_layout()
plt.show()