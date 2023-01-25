import numpy as np
import time
s = [[-1,0,0], [-1,1,0],[-1,0,1],[-1,1,1]]
sample = np.array(s)
w = np.random.random_sample(3)
# w = np.array([0,0,0])
d = np.array([-1,-1,-1,1])
cost_func_i = lambda x_i, w, d_i: np.dot(np.dot(x_i, w), d_i)
d_cost = lambda x, d: np.dot(d, x)
rate = 5e-2
# rate = 0.5
update_func = lambda x, w, d: w+(rate*d_cost(x, d))

s_mis = []
d_mis = []
for i, x in enumerate(sample):
    if cost_func_i(x, w, d[i]) <=0:
        s_mis.append(x)
        d_mis.append(d[i])
    print("cost:", cost_func_i(x, w, d[i]))
s_mis = np.array(s_mis)
d_mis = np.array(d_mis)
print(s_mis)
while len(s_mis>0):
    w = update_func(s_mis, w, d_mis)
    print("connection weight: ", w)
    time.sleep(1)
    s_mis = []
    d_mis = []
    for i, x in enumerate(sample):
        if cost_func_i(x, w, d[i]) <=0:
            s_mis.append(x)
            d_mis.append(d[i])
        print("cost:", cost_func_i(x, w, d[i]))
    s_mis = np.array(s_mis)
    d_mis = np.array(d_mis)

print("connection weight:", w)
