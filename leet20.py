class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sl = list(s)
        parens = list()
        square = list()
        curlyb = list()
        