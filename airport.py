#from __future__ import print_function
import cplex
import time
out_file_name='out.gz'
c=cplex.Cplex()
#out = c.set_results_stream('result.txt')

#out = c.set_results_stream('result.txt')
c.read('out.lp')
c.set_problem_name('problem0')
c.solve()
print '>>>>>>>>>',c.get_problem_name()
#print c.get_problem_type()
print("Solution status = ", c.solution.status[c.solution.get_status()])
print("Solution value  = ", c.solution.get_objective_value())
for j in range(c.variables.get_num()):
    print("Column %d:  Value = %10f  " % (j, c.solution.get_values()[j]))
#print out
#print c.get_stats()
#c.write('out.lp')
c.end


