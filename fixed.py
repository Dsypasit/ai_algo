import numpy as np
s = [[-1,0,0], [-1,1,0],[-1,0,1],[-1,1,1]]
sample = np.array(s)
w = np.random.random_sample(3)
# w = np.array([1.5,1,1])
d = np.array([-1, -1, -1, 1])
cost_func_i = lambda x_i, w, d_i: np.dot(np.dot(x_i, w), d_i)
d_cost = lambda x_i, d_i: np.dot(x_i, d_i)
update_w = lambda x_i, w, d_i: w + d_cost(x_i, d_i)

s_mis = []
d_mis = []
for i, x in enumerate(sample):
    if cost_func_i(x, w, d[i]) <= 0:
        s_mis.append(x)
s_mis = np.array(s_mis)

while len(s_mis) > 0:
    s_mis = []
    for i, x in enumerate(sample):
        print("cost: ", cost_func_i(x, w, d[i]))
        if cost_func_i(x, w, d[i]) <= 0:
            w = update_w(x, w, d[i])
            s_mis.append(x)
    s_mis = np.array(s_mis)

print("weight: ", w)

