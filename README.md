# RLC Circuit Transient Response Simulation

This project simulates the transient response of a Series RLC Circuit under different damping conditions using Python.

The simulation analyzes:

- Undamped Response
- Underdamped Response
- Critically Damped Response
- Overdamped Response

The project visualizes both:

- Capacitor Voltage Response
- Circuit Current Response

with additional exponential decay envelopes to clearly compare damping speed between different resistance values.

---

# Mathematical Model

The governing differential equation for a series RLC circuit is:

\[
L\frac{d^2i}{dt^2} + R\frac{di}{dt} + \frac{1}{C}i = 0
\]

or in capacitor voltage form:

\[
\frac{d^2v}{dt^2} + \frac{R}{L}\frac{dv}{dt} + \frac{1}{LC}v = 0
\]

where:

- \(L\) = Inductance
- \(C\) = Capacitance
- \(R\) = Resistance
- \(v(t)\) = Capacitor voltage
- \(i(t)\) = Circuit current

---

# Damping Conditions

The simulation includes four system conditions:

| State | Condition |
|---|---|
| Undamped | \(R = 0\) |
| Underdamped | \(R < R_c\) |
| Critically Damped | \(R = R_c\) |
| Overdamped | \(R > R_c\) |

Critical resistance is calculated using:

\[
R_c = 2\sqrt{\frac{L}{C}}
\]

---

# Features

- Numerical transient simulation
- Voltage and current visualization
- Exponential decay envelope comparison
- Clean subplot organization
- Engineering-focused mathematical comments
- Accurate derivative approximation using `np.gradient()`

---

# Technologies Used

- Python
- NumPy
- Matplotlib
- Pandas

---

# Project Structure

```bash
RLC-Transient-Simulation/
│
├── main.py
├── README.md
└── output_graphs/
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/RLC-Transient-Simulation.git
```

Move into the project directory:

```bash
cd RLC-Transient-Simulation
```

Install required libraries:

```bash
pip install numpy matplotlib pandas
```

---

# Run the Simulation

```bash
python main.py
```

---

# Output

The program generates:

1. Damped system responses:
   - Underdamped
   - Critically damped
   - Overdamped

2. Undamped oscillation response

Each state includes:
- Voltage response
- Current response
- Decay envelope visualization

---

# Numerical Method

Current is calculated numerically from capacitor voltage using:

\[
i(t) = C\frac{dv(t)}{dt}
\]

using:

```python
np.gradient(v, t, edge_order=2)
```

The parameter `edge_order=2` improves derivative accuracy near signal boundaries.

---

# Example Concepts Demonstrated

- Resonance
- Oscillation
- Energy dissipation
- Exponential decay
- Second-order differential systems
- Damping ratio behavior
- Natural frequency response

---

# Educational Purpose

This project is designed for:

- Electrical Engineering students
- Control Systems studies
- Circuit analysis courses
- Signal processing fundamentals
- Transient response visualization

---

# Author

Mohamed Saleh

Engineering & AI Enthusiast

---

# License

This project is open-source and available under the MIT License.
