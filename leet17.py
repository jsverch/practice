class Solution(object):
    def getlets(self, d):
        ldict =    {2: ['a', 'b', 'c'],
                    3: ['d', 'e', 'f'],
                    4: ['g', 'h', 'i'],
                    5: ['j', 'k', 'l'],
                    6: ['m', 'n', 'o'],
                    7: ['p', 'q', 'r', 's'],
                    8: ['t', 'u', 'v'],
                    9: ['w', 'x', 'y', 'z']
                    }
        return ldict[d]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        ldict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if digits == "":
            return list()
        else:
            return reduce(lambda acc, digit: [x + y for x in acc for y in ldict[digit]], digits, [''])


print Solution().letterCombinations("")
