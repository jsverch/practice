from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        k = str()
        sug = list()

        for i in range(0, len(searchWord)):
            k = k + searchWord[i]
            s = [p for p in products if p[0:len(k)] == k]
            sug.append(sorted(s)[0:3])
        return sug


obj = Solution()

products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

r = obj.suggestedProducts(products, searchWord)

print(r)
