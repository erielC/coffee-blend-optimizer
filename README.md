# coffee-blend-optimizer

# ☕ Coffee Blend Optimizer

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)](CONTRIBUTING.md)

A Python-based optimization system that finds the perfect combination of coffee beans to minimize cost while maintaining quality standards. Built with Pyomo, YAML configuration, and Pandas reporting.

## 🎯 Problem Statement

You run a coffee shop and need to create a house blend using 3 different coffee beans. Each bean has different costs, quality scores, and availability constraints. The challenge is to find the optimal blend that minimizes cost while meeting quality requirements and business constraints.

## 📊 Business Scenario

**Available Beans:**
- **Bean A (Premium)**: $12/kg, Quality 9/10, Max 50kg/week
- **Bean B (Standard)**: $8/kg, Quality 6/10, Max 100kg/week  
- **Bean C (Economy)**: $5/kg, Quality 4/10, Max 80kg/week

**Requirements:**
- Total blend: 100kg per week
- Minimum quality score: 6.0/10
- Each bean must be at least 10% of blend
- Premium beans cannot exceed 40% of blend

## 🚀 Features

- ✅ **YAML Configuration**: Easy-to-modify bean properties and constraints
- ✅ **Linear Programming**: Optimal solution using Pyomo optimization framework
- ✅ **Multiple Objectives**: Cost minimization and quality maximization modes
- ✅ **Sensitivity Analysis**: Test impact of price changes and constraint modifications
- ✅ **Clean Reporting**: Pandas-based results with CSV export
- ✅ **Extensible Design**: Easy to add new beans, constraints, or objectives

## 🛠️ Technology Stack

- **Python 3.8+**
- **Pyomo** - Optimization modeling
- **PyYAML** - Configuration management
- **Pandas** - Data analysis and reporting
- **NumPy** - Numerical computations
- **GLPK** - Open-source linear programming solver

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/coffee-blend-optimizer.git
cd coffee-blend-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install solver (choose one)
# Mac: brew install glpk
# Ubuntu: sudo apt-get install glpk-utils
# Windows: Download from https://sourceforge.net/projects/winglpk/
```

## 🏃‍♂️ Quick Start

```bash
# Run the basic optimization
python src/optimizer.py

# Run with custom configuration
python src/optimizer.py --config config/custom_beans.yaml

# Generate sensitivity analysis
python src/optimizer.py --sensitivity --range 20
```

## 📁 Project Structure

```
coffee-blend-optimizer/
├── README.md
├── requirements.txt
├── config/
│   ├── beans.yaml              # Bean properties and constraints
│   └── scenarios.yaml          # Different optimization scenarios
├── src/
│   ├── optimizer.py            # Main optimization engine
│   ├── data_loader.py          # YAML configuration loader
│   ├── reporter.py             # Results formatting and export
│   └── utils.py                # Helper functions
├── data/
│   └── sample_results.csv      # Example output
├── tests/
│   └── test_optimizer.py       # Unit tests
└── docs/
    └── optimization_guide.md   # Detailed documentation
```

## 💡 Usage Examples

### Basic Optimization
```python
from src.optimizer import CoffeeOptimizer

# Initialize with default configuration
optimizer = CoffeeOptimizer('config/beans.yaml')

# Solve for minimum cost
optimizer.solve(objective='minimize_cost')

# Display results
optimizer.print_results()
```

### Custom Scenarios
```python
# Solve for maximum quality
optimizer.solve(objective='maximize_quality')

# What-if analysis: 20% price increase
optimizer.sensitivity_analysis('cost', range_percent=20)

# Export results
optimizer.export_results('results/blend_analysis.csv')
```

## 📈 Example Output

```
╔═══════════════════════════════════╗
║     OPTIMAL COFFEE BLEND          ║
╚═══════════════════════════════════╝

🎯 Optimization Status: ✅ Optimal
💰 Total Cost: $735.00
⭐ Average Quality: 6.10/10

📊 Bean Composition:
┌─────────────────┬────────┬─────────────┐
│ Bean Type       │ Weight │ Percentage  │
├─────────────────┼────────┼─────────────┤
│ Bean A (Premium)│ 25.0kg │    25.0%    │
│ Bean B (Standard)│ 45.0kg │    45.0%    │
│ Bean C (Economy) │ 30.0kg │    30.0%    │
└─────────────────┴────────┴─────────────┘

✅ Constraints Status: All satisfied
   • Total weight: 100.0 kg
   • Quality requirement: 6.10 ≥ 6.00 ✅
   • Min bean usage: All beans ≥ 10% ✅
   • Max premium: 25% ≤ 40% ✅
```

## 🔬 Advanced Features

### Sensitivity Analysis
Test how changes in bean prices affect the optimal solution:
```bash
python src/optimizer.py --sensitivity cost --range 30
```

### Multiple Scenarios
Compare different optimization objectives:
```bash
python src/optimizer.py --compare-scenarios
```

### Custom Constraints
Add new business rules via YAML configuration:
```yaml
additional_constraints:
  max_single_origin: 0.6  # No bean > 60%
  seasonal_availability:   # Seasonal variations
    bean_a: [40, 50, 30, 45]  # Q1, Q2, Q3, Q4
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src

# Run specific test
python -m pytest tests/test_optimizer.py::test_basic_optimization
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Learning Resources

- [Pyomo Documentation](https://pyomo.readthedocs.io/)
- [Linear Programming Basics](https://en.wikipedia.org/wiki/Linear_programming)
- [Coffee Blending Industry Guide](docs/coffee_industry_background.md)

## 🐛 Troubleshooting

**Common Issues:**

1. **Solver not found**: Install GLPK or update solver path
2. **Infeasible solution**: Check if constraints are too restrictive
3. **Import errors**: Ensure all dependencies are installed in virtual environment

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Coffee industry data from International Coffee Organization
- Optimization techniques from operations research literature
- Inspired by real-world supply chain challenges

## 🔗 Related Projects

- [Supply Chain Optimizer](https://github.com/example/supply-chain)
- [Production Planning Tool](https://github.com/example/production-planning)
- [Inventory Management System](https://github.com/example/inventory-mgmt)

---

**Built with ☕ and optimization algorithms**

*For questions or support, please open an issue or contact [your-email@domain.com]*
