from random import randint
import time
import bisect

start_time = time.time()

# e = [2, 3, 4, 2, 3, 6, 8, 4, 5]
e = [10, 20, 30, 40, 50]

# e = list()

# for r in range(0, 200000):
#     e.append(randint(0, 200))

d = 3

# d = 3
warn = 0

h = list()

for i in range(0, len(e)):
    if len(h) > d:
        # h.remove(e[i-d])
        del h[bisect.bisect_left(h, e[i-d])]

    bisect.insort(h, e[i])
    # print "index : {}, value : {}".format(i, e[i])
    if i > d - 1:
        if d % 2:
            m = (d / 2)
            median = h[m]
        else:
            median = (h[(d/2) - 1] + h[(d / 2)]) / 2.0
        # print h
        # print "Median : {}, Value : {}".format(median, e[i])
        if e[i] >= (median * 2):
            warn += 1

print warn

print "Time : {}".format(time.time() - start_time)