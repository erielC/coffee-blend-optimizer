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

## 🛠️ Technology Stack

- **Python 3.8+**
- **Pyomo** - Optimization modeling
- **PyYAML** - Configuration management
- **Pandas** - Data analysis and reporting
- **NumPy** - Numerical computations

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/erielC/coffee-blend-optimizer.git
cd coffee-blend-optimizer

# Create conda environment

# Install dependencies

# Install solver (choose one)
```

## 🏃‍♂️ Quick Start

```bash
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

## 🐛 Troubleshooting

**Common Issues:**

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.
---


**Built with ☕ and optimization algorithms**

*For questions or support, please open an issue or contact [erielcabrera1234@gmail.com]
