from typing import List
import re


class Solution:
    def __init__(self):
        self.cardinal = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
                         "7": "Seven", "8": "Eight", "9": "Nine"}

        self.mults = {1: "", 2: "Thousand", 3: "Million", 4: "Billion"}
        self.teens = {"10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen",
                      "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen",
                      "18": "Eighteen", "19": "Nineteen"}
        self.ees = {"1": "Teen", "2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty", "6": "Sixty",
                    "7": "Seventy", "8": "Eighty", "9": "Ninety"}

    def Triplets(self, num: int) -> List:
        n = str(num)
        t = list()
        while n != '':
            t.append(n[-3:])
            n = n[0:-3]
        t.reverse()
        return t

    def SayIt(self, t: str, m: int):
        # print("Doing: {}".format(t))
        t = t.lstrip("0")
        s = ""
        if t == "":
            # print("Zero: {}".format(self.mults[m]))
            return self.mults[m]
        if len(t) == 3:
            s += self.cardinal[t[0]] + " Hundred "
            t = t[1:]
        if t == "00":
            s += " " + self.mults[m] + " "
            return "{}".format(s)
        if len(t) == 2:
            if 10 < int(t) < 20:
                s += self.teens[t]
            elif int(t) > 10:
                s += self.ees[t[0]] + " " + self.cardinal[t[1]]
            elif int(t) == 10:
                s += "Ten"
            elif int(t) < 10:
                s += self.cardinal[t[1]]
            s += " " + self.mults[m]
        else:
            s += self.cardinal[t]
            s += " " + self.mults[m]
        if m != 1:
            s += " "
        return "{}".format(s)

    def numberToWords(self, num: int) -> str:
        a = ""
        if num == 0:
            return "Zero"
        trips = self.Triplets(num)
        m = len(trips)
        for t in trips:
            a += self.SayIt(t, m)
            m -= 1
        a = re.sub(' +', ' ', a)
        a = re.sub('Million Thousand', 'Million ', a)
        a = re.sub('Billion Million', 'Billion ', a)
        a = re.sub('Billion Thousand', 'Billion ', a)
        return a.strip()
