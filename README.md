# AIRPORT_cplex

generate_coordinate产生整数随机坐标

coordinat.txt文件用于存储随机产生的坐标点

lingo_out & cplex_out.txt为复制lingo和cplex程序输出结果

process_lingo_out & process_cplex_out 用来处理结果产生路线以及将其绘图

vrptw.mod 是cplex模型文件，将generate_coordinate产生的输出结果替换文件中的数据部分即可

lingo_vrp.txt是复制的lingo代码，可以将其复制到lingo编译器运行
