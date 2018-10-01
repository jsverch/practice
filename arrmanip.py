
n = 100000

arr = list()

q =[(20345, 61111, 3518), (30000, 50000, 746326), (1, 8, 1), (5, 9, 15)]

# q = [(1, 2, 100),
#      (2, 5, 100),
#      (3, 4, 100)]

for x in range(0, n):
    arr.append(0)

for i in range(0, len(q)):
    for j in range(q[i][0] - 1, q[i][1]):
        print "adding {} to {} @ {}".format(q[i][2], arr[j], j)
        arr[j] += q[i][2]


print max(arr)
