from typing import List
import re


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = re.compile('^\d+$')
        # letrs  = re.compile('^[a-zA-Z]+$')
        d_l = list()
        l_d = dict()
        l_l = list()

        for l in logs:
            # print("Try: {}".format(l.split()[1:2]))
            if bool(re.search(digits, l.split()[1:2][0])):
                d_l.append(l)
            else:
                l_d[l.split()[0]] = l.split()[1:]

        t = sorted(l_d.items(), key=lambda item: item[1])
        for x in t:
            l_l.append('{} {}'.format(x[0], ' '.join(x[1][0:])))
        # print(d_l)
        return l_l+d_l


obj = Solution()

# r_logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
r_logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]
r = obj.reorderLogFiles(r_logs)

print(r)
