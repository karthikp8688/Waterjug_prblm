from typing import Dict, List, Callable, Any

class CSP:
    def __init__(self):
        self.variables: List[str] = []
        self.domains: Dict[str, List[Any]] = {}
        self.constraints: Dict[str, List[Callable]] = {}

    def add_variable(self, variable: str, domain: List[Any]):
        self.variables.append(variable)
        self.domains[variable] = domain
        self.constraints[variable] = []

    def add_constraint(self, variables: List[str], constraint: Callable):
        for var in variables:
            self.constraints[var].append(constraint)

    def is_consistent(self, variable: str, assignment: Dict[str, Any]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint(assignment):
                return False
        return True

    def backtrack(self, assignment: Dict[str, Any]) -> Dict[str, Any] | None:
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        var = unassigned[0]

        for value in self.domains[var]:
            local_assignment = assignment.copy()
            local_assignment[var] = value

            if self.is_consistent(var, local_assignment):
                result = self.backtrack(local_assignment)
                if result is not None:
                    return result

        return None

    def solve(self):
        return self.backtrack({})

# ------------------- DYNAMIC INPUT -------------------

def main():
    csp = CSP()

    # Step 1: Get variables and domains
    n_vars = int(input("Enter number of variables: "))
    for _ in range(n_vars):
        var_name = input("Variable name: ")
        domain_input = input(f"Enter domain values for {var_name} (comma-separated): ")
        domain = [int(x.strip()) for x in domain_input.split(",")]
        csp.add_variable(var_name, domain)

    # Step 2: Get constraints
    n_constraints = int(input("Enter number of constraints: "))
    print("Constraint format: use Python syntax, e.g., A != B or A < C")
    for i in range(n_constraints):
        constraint_input = input(f"Constraint {i+1}: ")

       
        def make_constraint(expr):
            return lambda a: eval(expr, {}, a)
        
        csp.add_constraint(list(csp.variables), make_constraint(constraint_input))

    # Step 3: Solve
    solution = csp.solve()
    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()

output :
Enter number of variables: 2
Variable name: A
Enter domain values for A (comma-separated): 1,2,3
Variable name: B
Enter domain values for B (comma-separated): 1,2,3
Enter number of constraints: 1
Constraint 1: A != B
Solution found:
{'A': 1, 'B': 2}

