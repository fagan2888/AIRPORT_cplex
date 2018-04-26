infilename='lingo_out'
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D
import random


def process_solution(solution_list):
    paths = []
    deleted = []
    for solut in solution_list:
        if solut[0] == 1:
            paths.append([solut[0], solut[1]])
            deleted.append(solut)
    for d in deleted:
        solution_list.remove(d)
    #print paths

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
    for i in range(len(paths)):
        print 'paths'+str(i)+'                                       ',paths[i]
    return paths
def get_paths():
    f=open(infilename,'r')
    tot_text=f.read()
    solutions=re.findall('X\( \d+, \d+\)        \d',tot_text)
    obj_value=re.findall('Objective value:                              \d+\.\d+',tot_text)[0]
    solution_list=[]
    for line in solutions:
        line=str(line)
        arcs=re.findall('(?<=X\( )\d+, \d+(?=\))',line)[0]
        i=int(re.findall('\d+(?=,)',arcs)[0])
        j=int(re.findall('(?<=, )\d+',arcs)[0])
        flag=int(line[-1:])
        if flag==1:
            solution_list.append([i,j])
            #print i,j,flag
    paths=process_solution(solution_list)
    print obj_value
    return paths
def plot_path(coord_list,paths):
    figure, ax = plt.subplots()
    ax.set_xlim(left=0, right=tot*1.3)
    ax.set_ylim(bottom=0, top=tot*1.3)
    for i in range(tot+1):
        ax.scatter(coord_list[i][0], coord_list[i][1])
        pass
    #generate the random color
    colors=[]
    color_letter = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(10):
        color_letter.append(str(i))
    for i in range(len(paths)):
        color_str = ''
        for i in range(6):
            color_str = color_str + color_letter[random.randint(0, 15)]
        colors.append('#'+color_str)
        
    for path in paths:
        for j in range(len(path)):
            path[j] -= 1
        for point_no in range(len(path)-2):
            #print point_no
            #print  coord_list[path[point_no]][0], coord_list[path[point_no]][1],coord_list[path[point_no+1]][0], coord_list[path[point_no+1]][1]

            line1 = [(coord_list[path[point_no]][0], coord_list[path[point_no]][1]), (coord_list[path[point_no+1]][0], coord_list[path[point_no+1]][1])]
            (line1_xs, line1_ys) = zip(*line1)
            ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color=colors[paths.index(path)]))
    plt.plot()
    plt.show()
    pass

tot=100
#coord=0
coord_line=open('coordinate.txt','r').readline()
content=coord_line.split('], [')
coord_list=[]
import re
for coo in content:
    coord_list.append([int(re.findall('\d+(?=,)',coo)[0]),int(re.findall('(?<=, )\d+',coo)[0])])
coord_list[0:0]=[[0,0]]
#coord=[[0, 0],[9, 12], [7, 2], [11, 11], [8, 9], [11, 7], [3, 7], [4, 10], [12, 4], [2, 4], [10, 10], [7, 11], [3, 4], [7, 12],[6, 11], [9, 7], [8, 8], [7, 6], [12, 8], [2, 6], [6, 10]]
paths=get_paths()
plot_path(coord_list,paths)
