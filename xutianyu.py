file='movies.csv'
file_out='out.csv'
f=open(file,'r')
f2=open(file_out,'a')
lines=f.readlines()
for line in lines:
    #print line
    f2.write(line.replace('|',','))