from __future__ import print_function
import cplex

my_obj = [1.0, 2.0, 3.0]
my_ub = [40.0, 60.0, 90.0]
my_variables = ["x1", "x2", "x3"]
my_rhs = [20.0, 30.0, 40.0]
my_sense = "ELG"
rows = [
        [my_variables, [-1.0, 1.0, 1.0]],
        [my_variables, [1.0, -3.0, 1.0]],
        [my_variables, [1.0, 1.0, 1.0]]
       ]

cpl = cplex.Cplex()
cpl.objective.set_sense(cpl.objective.sense.minimize)
cpl.variables.add(obj=my_obj, ub=my_ub, names=my_variables)
cpl.linear_constraints.add(lin_expr=rows, senses=my_sense, rhs=my_rhs)
cpl.solve()

print("Solution status = ", cpl.solution.status[cpl.solution.get_status()])
print("Solution value  = ", cpl.solution.get_objective_value())
for j in range(cpl.variables.get_num()):
    print("Column %d:  Value = %10f  " % (j, cpl.solution.get_values()[j]))

cpl.write("Modle.lp")