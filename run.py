from pyomo.environ import ConcreteModel, Var, Param, NonNegativeReals, Objective, Constraint, minimize, Set, SolverFactory


# Data Organization
beans = ['A', 'B', 'C']
costs = {'A': 12, 'B': 8, 'C': 5}
quality = {'A': 9, 'B': 6, 'C': 4}
max_supply = {'A': 50, 'B': 100, 'C': 80}

# Parameters
TOTAL_WEIGHT = 100
MIN_QUALITY = 6.0
MIN_BEAN_AMOUNT = 10
MAX_PREMIUM_AMOUNT = 40

# Model Creation
model = ConcreteModel()

# Sets
model.beans = Set(initialize=beans)

# Parameters
model.cost = Param(model.beans, initialize=costs)
model.quality = Param(model.beans, initialize=quality)
model.max_supply = Param(model.beans, initialize=max_supply)

# Decision Variables
model.x = Var(model.beans, domain=NonNegativeReals)

# Rule Functions
def weight_rule(model):
    # Total weight must equal 100kg
    return sum(model.x[i] for i in model.beans) == TOTAL_WEIGHT

def quality_rule(model):
    # Quality must be greater than or equal to 6.0
    return (sum(model.quality[i] * model.x[i] for i in model.beans) / TOTAL_WEIGHT) >= MIN_QUALITY

def premium_limit_rule(model):
    # Bean A (premium) must not exceed 40% of total blend
    return model.x['A'] <= MAX_PREMIUM_AMOUNT

# Indexed Rules
def min_usage_rule(model, beans):
    # Each bean must be utilized atleast in 10% of the total blend
    return model.x[beans] >= MIN_BEAN_AMOUNT

def supply_limit_rule(model, beans):
    # Max supply of each bean respectively per week
    return model.x[beans] <= model.max_supply[beans]

# Contraints created via rules
model.weight_constraint = Constraint(rule=weight_rule)
model.quality_constraint = Constraint(rule=quality_rule)
model.max_premium_constraint = Constraint(rule=premium_limit_rule)
model.min_usage_constraint = Constraint(model.beans, rule=min_usage_rule)
model.supply_limit_constraint = Constraint(model.beans, rule=supply_limit_rule)

#Objective Rule
def min_cost_rule(model):
    # Produces a quality blend but has to be minimal costs
    return sum(model.cost[i] * model.x[i] for i in model.beans)

model.obj = Objective(rule=min_cost_rule, sense=minimize)

# GLPK SOLVER
solver = SolverFactory('glpk')
results = solver.solve(model)

# Display results
print("="*50)
print("COFFEE BLEND OPTIMIZATION RESULTS")
print("="*50)
print(f"Solver Status: {results.solver.termination_condition}")

if results.solver.termination_condition == 'optimal':
    print(f"\nOptimal Solution Found!")
    total_cost = 0
    
    for bean in model.beans:
        amount = model.x[bean].value
        cost = model.cost[bean] * amount
        percentage = (amount / TOTAL_WEIGHT) * 100
        total_cost += cost
        
        print(f"Bean {bean}: {amount:.1f} kg ({percentage:.1f}%) - Cost: ${cost:.2f}")
    
    print(f"\nTotal Cost: ${total_cost:.2f}")
    
    # Calculate final quality
    final_quality = sum(model.quality[bean] * model.x[bean].value for bean in model.beans) / TOTAL_WEIGHT
    print(f"Final Quality Score: {final_quality:.2f}")
else:
    print("No optimal solution found!")
