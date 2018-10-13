from timeit import default_timer as timer


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s) == sorted(t):
            return True
        else:
            return False

        # lt = list(t)
        # for c in s:
        #     try:
        #         lt.remove(c)
        #     except:
        #         return False
        # if len(lt) == 0:
        #     return True
        # else:
        #     return False


start = timer()
print Solution().isAnagram("foobar", "barfoo")
end = timer()

print "Elapsed : {}".format(end-start)