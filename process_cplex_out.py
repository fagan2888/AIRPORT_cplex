infilename = 'cplex_out.txt'
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D
import random
import numpy as np

def process_solution(solution_list):
    paths = []
    deleted = []
    # find the path section start from 0 point
    for solut in solution_list:
        if solut[0] == 0:
            paths.append([solut[0], solut[1]])
            deleted.append(solut)
    for d in deleted:
        solution_list.remove(d)
    # print paths

    print '>>>>>>>>>'
    for path in paths:
        flag = 1
        while flag:
            flaggg = 0
            for solut in solution_list:
                if solut[0] == path[-1]:
                    flaggg = 1  # means that we can still find path ,continue
                    path.append(solut[1])
                    solution_list.remove(solut)
                    break
            if flaggg == 0:
                flag = 0
                break
            else:
                flaggg = 0
                pass
    i=0
    while i <len(paths):
        if paths[i]==[0,0]:
            paths.remove(paths[i])
            i-=1 # or the list will out of range
        else:
            print 'paths' + str(i) + '                          ', paths[i]
            tot_length=0
            for j in range(len(paths[i])-2):
                tot_length+=round(np.sqrt(np.square(coord_list[paths[i][j]][0] - coord_list[paths[i][j+1]][0]) + np.square(coord_list[paths[i][j]][1] - coord_list[paths[i][j+1]][1])), 2)
            print '     tot_dist=',tot_length,
            length_to_last=round(np.sqrt(np.square(coord_list[paths[i][0]][0] - coord_list[paths[i][-2]][0]) + np.square(coord_list[paths[i][0]][1] - coord_list[paths[i][-2]][1])), 2)
            print '     dist to last point=',length_to_last
            detour=round(tot_length/length_to_last,2)
            print '     detour=',detour
            print '>>>>',detour<=1.3,'\n'
            if detour>1.3:
                print '''
                
                #######  ######  ######  ######  ######
                ##   ##  ##   #  ##   #  ##  ##  ##   #
                #######  ######  ######  ##  ##  ######
                ##       # ##    # ##    ##  ##  # ##
                #######  #   ##  #   ##  ######  #   ##
                
                   '''
        i+=1
    return paths


def get_paths():
    f = open(infilename, 'r')
    tot_text = f.read().replace('\n','').replace('                 [','[').replace('                 ',' ')
    solutions = re.findall('(?<=x = \[).*?(?=\];)', tot_text)[0].split(']             [')
    solution_list = []

    for i in range(len(solutions)):
        single_line=re.findall('\[\d.*?\]',solutions[i])
        ##print single_line
        for one_arcs in single_line:
            answer_list=re.findall('\d',one_arcs)
            for answer in answer_list:
                if answer=='1':
                    solution_list.append([i,single_line.index(one_arcs)])
    obj_value = re.findall('MILP objective *\d+\.\d+e\+\d+', tot_text)[0]
    print solution_list
    paths = process_solution(solution_list)

    print obj_value
    return paths


def plot_path(coord_list, paths):
    figure, ax = plt.subplots()
    #ax.set_xlim(left=0, right=tot * 1.3)
    #ax.set_ylim(bottom=0, top=tot * 1.3)
    for i in range(tot + 1):
        ax.scatter(coord_list[i][0], coord_list[i][1])
        pass
    # generate the random color
    colors = []
    color_letter = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(10):
        color_letter.append(str(i))
    for i in range(len(paths)):
        color_str = ''
        for i in range(6):
            color_str = color_str + color_letter[random.randint(0, 15)]
        colors.append('#' + color_str)

    for path in paths:
        #for j in range(len(path)):
        #    path[j] -= 1
        for point_no in range(len(path) - 2):
             #print point_no
             #print  coord_list[path[point_no]][0], coord_list[path[point_no]][1],coord_list[path[point_no+1]][0], coord_list[path[point_no+1]][1]

            line1 = [(coord_list[path[point_no]][0], coord_list[path[point_no]][1]), (coord_list[path[point_no + 1]][0], coord_list[path[point_no + 1]][1])]
            (line1_xs, line1_ys) = zip(*line1)
            ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color=colors[paths.index(path)]))
    plt.plot()
    plt.show()
    pass


tot = 9
# coord=0
coord_line = open('coordinate_cplex_full.txt', 'r').readline()
content = coord_line.split('],[')
coord_list = []
import re
for coo in content:
    #print coo
    #print(re.findall('\d+\.\d+(?=,)', coo)[0])
    coord_list.append([float(re.findall('\d+\.\d+(?=,)', coo)[0]), float(re.findall('(?<=,)\d+\.\d+', coo)[0])])
#coord_list[0:0] = [[0, 0]]
coord_list[0:0] = [[103.955542,30.569893]]

paths = get_paths()
plot_path(coord_list, paths)
