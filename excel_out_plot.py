infile = 'match_shortsee.txt'
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import Line2D
import random
import numpy as np

def small_process(paths):
    i = 0
    while i < len(paths):
        if paths[i] == [0, tot+1]:
            paths.remove(paths[i])
            i -= 1  # or the list will out of range
        else:
            print 'paths' + str(i) + '                          ', paths[i]
            tot_length = 0
            for j in range(len(paths[i]) - 2):
                tot_length += round(np.sqrt(
                    np.square(coord_list[paths[i][j]][0] - coord_list[paths[i][j + 1]][0]) + np.square(
                        coord_list[paths[i][j]][1] - coord_list[paths[i][j + 1]][1])), 2)
            print '     tot_dist=', tot_length,
            length_to_last = round(np.sqrt(
                np.square(coord_list[paths[i][0]][0] - coord_list[paths[i][-2]][0]) + np.square(
                    coord_list[paths[i][0]][1] - coord_list[paths[i][-2]][1])), 2)
            print '     dist to last point=', length_to_last
            detour = round(tot_length / length_to_last, 2)
            print '     detour=', detour
            print '>>>>', detour <= 1.3, '\n'
            if detour > 1.3:
                print '''

                #######  ######  ######  ######  ######
                ##   ##  ##   #  ##   #  ##  ##  ##   #
                #######  ######  ######  ##  ##  ######
                ##       # ##    # ##    ##  ##  # ##
                #######  #   ##  #   ##  ######  #   ##

                   '''
        i += 1
    return paths

def plot_path(coord_list, paths):
    figure, ax = plt.subplots()

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
        # for j in range(len(path)):
        #    path[j] -= 1

        for point_no in range(len(path) - 2):
            # print point_no
            # print  coord_list[path[point_no]][0], coord_list[path[point_no]][1],coord_list[path[point_no+1]][0], coord_list[path[point_no+1]][1]

            line1 = [(coord_list[path[point_no]][0], coord_list[path[point_no]][1]),
                     (coord_list[path[point_no + 1]][0], coord_list[path[point_no + 1]][1])]
            (line1_xs, line1_ys) = zip(*line1)
            ax.add_line(Line2D(line1_xs, line1_ys, linewidth=1, color=colors[paths.index(path)]))
        #print path
    plt.plot()
    plt.show()
        #raw_input()
    pass

def get_route():
    routes=[]
    f=open(infile,'r')
    text=f.readlines()
    for line in text[1:]:
        points=re.findall('\d+',line)
        cache=[0]
        for point in points:
            cache.append(int(point))
        cache.append(92)
        routes.append(cache)
    return routes

coord_line = open('coordinate_cplex_full.txt', 'r').readline()
content = coord_line.split('],[')
coord_list = []
import re
for coo in content:
    coord_list.append([float(re.findall('\d+\.\d+(?=,)', coo)[0]), float(re.findall('(?<=,)\d+\.\d+', coo)[0])])
coord_list[0:0] = [[103.955542, 30.569893]]



tot=91

routes=[[0, 92], [0, 13, 92], [0, 92], [0, 8, 92], [0, 43, 92], [0, 12, 92], [0, 92], [0, 92], [0, 75, 92], [0, 92], [0, 56, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 17, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 10, 92], [0, 92], [0, 92], [0, 34, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 68, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 14, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 32, 92], [0, 22, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 92], [0, 45, 92], [0, 92], [0, 92], [0, 92], [0, 50, 92]]

routes=get_route()
print routes
raw_input()
paths=small_process(routes)
plot_path(coord_list, paths)














