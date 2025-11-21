# Operations Research Solver 🎯

Advanced **linear programming** and **optimization solver** featuring the **Simplex Method**, transportation problems, assignment problems, and sensitivity analysis. Perfect for operations research, production planning, and resource allocation problems.

---

## 🌟 Features

### ✅ Linear Programming
- **Simplex Method** (Standard & Two-Phase)
- **Graphical Method Solver** (2D visualization)
- **Duality Theory** Implementation
- **Sensitivity Analysis** (Shadow prices, reduced costs)
- **Big-M Method** for artificial variables

### ✅ Specialized Algorithms
- **Transportation Problem** (Vogel's & MODI Method)
- **Assignment Problem** (Hungarian Algorithm)
- **Integer Programming** (Branch & Bound)
- **Network Flow Problems**

### ✅ Additional Features
- Problem verification and validation
- Solution feasibility checking
- Multiple solution detection
- Unbounded problem detection
- Infeasible problem handling

---

## 📦 Installation

### Prerequisites
- Python 3.7+
- NumPy
- Pandas
- Matplotlib (for visualization)

### Setup
```bash
# Clone repository
git clone https://github.com/jalel-masmoudi/operations-research-solver.git
cd operations-research-solver

# Install dependencies
pip install -r requirements.txt

# Verify installation
python3 -m pytest tests/
```

---

## 💡 Quick Start Examples

### Example 1: Simple Linear Programming

```python
from solver import SimplexSolver
import numpy as np

# Maximize: 3x + 2y
# Subject to:
#   x + y <= 4
#   x <= 2
#   y <= 3
#   x, y >= 0

solver = SimplexSolver()
objective = [3, 2]  # Coefficients to maximize
constraints = [
    ([1, 1], '<=', 4),
    ([1, 0], '<=', 2),
    ([0, 1], '<=', 3)
]

result = solver.solve(objective, constraints, maximize=True)
print(f"Optimal Value: {result['optimal_value']}")
print(f"Solution: x={result['x']}, y={result['y']}")
```

### Example 2: Transportation Problem

```python
from solver import TransportationSolver

solver = TransportationSolver()

# Supply at sources: [100, 150, 120]
# Demand at destinations: [80, 90, 70, 30]
# Cost matrix (4x3)
costs = [
    [4, 6, 8, 10],
    [5, 4, 7, 8],
    [6, 5, 4, 9]
]

solution = solver.solve(supply=[100, 150, 120],
                       demand=[80, 90, 70, 30],
                       costs=costs)

print(f"Minimum Cost: {solution['total_cost']}")
print(f"Allocation:\n{solution['allocation']}")
```

### Example 3: Assignment Problem

```python
from solver import AssignmentSolver

solver = AssignmentSolver()

# Cost matrix for assigning 4 workers to 4 jobs
costs = [
    [10, 14, 16, 13],
    [12, 15, 13, 11],
    [9, 12, 12, 14],
    [11, 13, 15, 12]
]

assignment = solver.solve(costs)
print(f"Minimum Cost: {assignment['total_cost']}")
print(f"Assignment: {assignment['assignment']}")
```

---

## 🧮 Algorithm Details

### Simplex Method

**Two-Phase Method Process:**

Phase 1: Find a feasible solution using artificial variables
```
Standard Form Conversion:
  Minimize c^T * x
  Subject to: Ax = b, x >= 0
```

Phase 2: Optimize from the feasible solution
```
Optimality Check:
  If c_j - z_j <= 0 for all j: OPTIMAL
  Otherwise: Enter entering variable, perform pivot operation
```

**Tableau Representation:**
```
|  Basis  | x1 | x2 | ... | RHS |
|---------|----|----|-----|-----|
|  s1     | a11| a12| ... | b1  |
|  s2     | a21| a22| ... | b2  |
|  ...    | ...|... |     | ... |
|  z      | c1 | c2 | ... | 0   |
```

### Transportation Problem

**Vogel's Approximation Method (VAM):**
1. Calculate penalties for each row/column
2. Select maximum penalty
3. Allocate minimum supply/demand to minimum cost cell
4. Repeat until allocation complete
5. Verify optimality using MODI method

### Hungarian Algorithm (Assignment)

**Steps:**
1. Subtract minimum of each row from all row elements
2. Subtract minimum of each column from all column elements
3. Cover all zeros with minimum number of lines
4. If lines = n: OPTIMAL
5. Otherwise: Update matrix and repeat

---

## 📂 Project Structure

```
operations-research-solver/
├── solver/
│   ├── __init__.py
│   ├── simplex.py          # Simplex method
│   ├── transportation.py   # Transportation problem
│   ├── assignment.py       # Assignment problem
│   ├── graphical.py        # 2D graphical method
│   ├── validators.py       # Input validation
│   └── utils.py            # Utility functions
├── examples/
│   ├── simplex_example.py
│   ├── transportation_example.py
│   ├── assignment_example.py
│   └── sensitivity_example.py
├── tests/
│   ├── test_simplex.py
│   ├── test_transportation.py
│   ├── test_assignment.py
│   └── test_validators.py
├── visualizations/
│   ├── plot_feasible_region.py
│   ├── plot_sensitivity.py
│   └── plot_convergence.py
├── requirements.txt
└── README.md
```

---

## 📊 Problem Types Solved

### 1. Production Optimization
```
Maximize: 5x₁ + 4x₂ (profit)
Subject to:
  2x₁ + 3x₂ <= 12 (labor hours)
  x₁ + 2x₂ <= 8 (material)
  x₁, x₂ >= 0
```

### 2. Diet Problem
```
Minimize: 0.5x₁ + 0.4x₂ + 0.3x₃ (cost)
Subject to:
  5x₁ + 2x₂ + 3x₃ >= 10 (calories)
  1x₁ + 1x₂ + 1x₃ >= 3 (protein)
  x₁, x₂, x₃ >= 0
```

### 3. Blending Problem
```
Minimize: c₁x₁ + c₂x₂ + ... (cost)
Subject to:
  x₁ + x₂ + ... = required_amount
  Quality constraints
  x_i >= 0
```

### 4. Transportation Network
```
Minimize: Total transportation cost
Subject to:
  Supply constraints
  Demand constraints
  Non-negativity
```

---

## 🔍 Output Analysis

Each solution provides:

### Basic Solution
```python
result = {
    'optimal_value': 18.5,        # Maximum/Minimum achieved
    'variables': [2.5, 3.0],      # Optimal x values
    'status': 'OPTIMAL',
    'iterations': 3
}
```

### Sensitivity Analysis
```python
sensitivity = {
    'shadow_prices': [1.5, 0, 2.0],          # Dual values
    'reduced_costs': [0, 0.5, 0],            # Non-basic variable costs
    'ranges': {
        'objective': [(2, 8), (1, 5)],       # RHS ranges
        'rhs': [(3, 6), (2, 10)]              # Coefficient ranges
    }
}
```

---

## 🧪 Testing

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific test
python3 -m pytest tests/test_simplex.py::test_maximization

# Generate coverage report
pytest --cov=solver tests/

# Run performance benchmarks
python3 benchmarks/performance_test.py
```

---

## 📊 Complexity Analysis

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Simplex | O(2^n) worst case | O(m*n) | Polynomial average |
| Transportation (VAM+MODI) | O(n³) | O(m*n) | Efficient in practice |
| Assignment (Hungarian) | O(n³) | O(n²) | Optimal |
| Graphical Method | O(vertices) | O(n) | Limited to 2D |

---

## 📈 Visualization

### Plot Feasible Region (2D)
```python
from visualizations import plot_feasible_region

constraints = [
    ([1, 1], '<=', 4),
    ([1, 0], '<=', 2),
    ([0, 1], '<=', 3)
]
objective = [3, 2]

plot_feasible_region(constraints, objective)
```

### Sensitivity Analysis Chart
```python
from visualizations import plot_sensitivity

sensitivity_ranges = {...}
plot_sensitivity(sensitivity_ranges)
```

---

## 🤝 Contributing

Contributions welcome! Potential improvements:

- [ ] Interior point methods
- [ ] Quadratic programming
- [ ] Stochastic programming
- [ ] Network optimization algorithms
- [ ] Performance optimizations
- [ ] More examples and tutorials

---

## 📚 Learning Resources

**Books:**
- "Operations Research: An Introduction" - Hamdy Taha
- "Linear Programming" - Vanderbei
- "Introduction to Operations Research" - Hillier & Lieberman

**Online:**
- NIST Handbook of Mathematical Functions
- MIT OpenCourseWare - Optimization
- Coursera - Operations Research Specialization

---

## 🐛 Known Limitations

- Limited to 2D graphical visualization
- No quadratic programming support yet
- Large-scale problems may require optimization
- Integer constraints require Branch & Bound

---

## 📄 License

MIT License - Open for educational and commercial use

---

## 👤 Author

**Jalel Masmoudi**  
Computer Science Student | North American University of Sfax  
Specialization: Operations Research

---

*Last Updated: November 2025*  
*For issues, questions, or contributions, please open an issue or PR!*
