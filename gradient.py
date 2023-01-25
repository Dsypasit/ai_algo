import numpy as np
sample = np.array([[1,0,0], [1,1,0], [1,0,1], [-1,1,1]])
d = np.array([-1,-1,-1,1])
w = np.random.random_sample(3)
cost_func = lambda x, w: 0.5*sum(d-np.dot(x, w))
d_cost = lambda x, w: -1*sum(np.dot(d-np.dot(x, w), x))
rate = 0.01
update_func = lambda x, w: w-rate*d_cost(x, w)

for i in range(100):
    w = update_func(sample, w)
    print("cost: ", cost_func(sample, w))

print("weight:", w)
