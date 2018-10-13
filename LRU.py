class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # create.. something.. of size <capacity>
        self.capacity = capacity
        self.cache = dict()
        self.used = list()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        # print "Used: {}".format(self.used)

        try:
            self.cache[key]
        except KeyError:
            return -1
        else:
            # do something for usage
            self.used.remove(key)
            self.used.append(key)
            return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print "Used: {}".format(self.used)

        if key in self.cache.keys():
            self.cache[key] = value
            self.used.remove(key)
            self.used.append(key)
            return

        if len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            del self.cache[self.used[0]]
            del self.used[0]
            self.cache[key] = value

        if key in self.used:
            self.used.remove(key)
            self.used.append(key)
        else:
            self.used.append(key)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)

print "C:{} : U:{}".format(obj.cache, obj.used)
print obj.get(2)
print "C:{} : U:{}".format(obj.cache, obj.used)
obj.put(2,6)
print "C:{} : U:{}".format(obj.cache, obj.used)
print obj.get(1)
print "C:{} : U:{}".format(obj.cache, obj.used)
obj.put(1,5)
print "C:{} : U:{}".format(obj.cache, obj.used)
obj.put(1,2)
print "C:{} : U:{}".format(obj.cache, obj.used)
print obj.get(1)
print "C:{} : U:{}".format(obj.cache, obj.used)
print obj.get(2)
print "C:{} : U:{}".format(obj.cache, obj.used)


exit()

obj.put(1, 1)
print obj.cache
obj.put(2, 2)
print obj.cache

print obj.get(1)
obj.put(3, 3)
print obj.cache

print obj.get(2)
obj.put(4, 4)
print obj.cache

print obj.get(1)
print obj.get(3)
print obj.get(4)
