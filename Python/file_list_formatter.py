import math

f_op = open("input.dat", "r")

ll = f_op.readlines()

x_raw = []
f = []
x = []
xx = []

lenn = len(x)

for z in ll:
    x_raw.append(z.split(' ')[0])

x = [a.replace('\n','') for a in x_raw]

for v in range(len(x)):
    xx.append(float(x[v]))

for c in range(len(x)):
    f.append(xx[c] * math.sin(2 * xx[c]))

f_ww = open("output.dat", "w")

for b in f:
    
    f_ww.write(str(b))


f_op.close
f_ww.close
