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

Clone the repository:
```bash
git clone https://github.com/erielC/coffee-blend-optimizer.git
```

Create a conda enviorment using the environment.yml file provided:
```bash
conda env create -f environment.yml 
```

Activate environment:
```bash
conda activate cf
```
## 🏃‍♂️ Quick Start

Once created the conda environment and it is active then simply:

```bash
python run.py
```

## 📁 Project Structure

## 📈 Example Output
```bash
==================================================
COFFEE BLEND OPTIMIZATION RESULTS
==================================================
Solver Status: optimal

Optimal Solution Found!
Bean A: 36.0 kg (36.0%) - Cost: $432.00
Bean B: 10.0 kg (10.0%) - Cost: $80.00
Bean C: 54.0 kg (54.0%) - Cost: $270.00

Total Cost: $782.00
Final Quality Score: 6.00
```
## 🐛 Troubleshooting

**Common Issues:**

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.
---


**Built with ☕ and optimization algorithms**

*For questions or support, please open an issue or contact [erielcabrera1234@gmail.com]
