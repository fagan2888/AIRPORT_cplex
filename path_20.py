import cplex
import numpy as np

tot=10
driver_num=4
coord_list=[[9, 12], [7, 2], [11, 11], [8, 9], [11, 7], [3, 7], [4, 10], [12, 4], [2, 4], [10, 10], [7, 11], [3, 4], [7, 12], [6, 11], [9, 7], [8, 8], [7, 6], [12, 8], [2, 6], [6, 10]]
dist=[[0]*(tot+2) for i in range(tot+2)]
x=[[[0]*driver_num for i in range(tot+2)]for j in range(tot+2)]

print x
def set_constraint():
    #c1:every passenger need to be driven
    for i in range(tot):





for i in range(tot):
    for j in range(tot):
        dist[i+1][j+1]= round(np.sqrt(np.square(coord_list[i][0]-coord_list[j][0])+np.square(coord_list[i][1]-coord_list[j][1])),2)

for j in range(tot):
    dist[0][j + 1] = round(np.sqrt(np.square(coord_list[j][0]) + np.square(coord_list[j][1])), 2)


for i in range(tot+2):
    print dist[i]

cpl=cplex.Cplex()
cpl.objective.set_sense(cpl.objective.sense.minimize)
my_obj=[1]*(tot+2)*(tot+2)*(driver_num)
cpl.variables.add(obj=my_obj,)
set_constraint()


'''
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

print"Solution status = ", cpl.solution.status[cpl.solution.get_status()]
print"Solution value  = ", cpl.solution.get_objective_value()
for j in range(cpl.variables.get_num()):
    print"Column %d:  Value = %10f  " % (j, cpl.solution.get_values()[j])

#cpl.write("Modle.lp")'''