class Solution:
    def addBinary(self, a: str, b: str) -> str:
        newA, newB, newAB, c,difference = list(a), list(b), "", "", abs(len(a)-len(b))
        if len(newA) > len(newB):
            while difference > 0:
                newB.insert(0, "0")
                difference -= 1
        elif len(newB) > len(newA):
            while difference > 0:
                newA.insert(0, "0")
                difference -=1
        for i in range(len(newA)-1, -1, -1):
            if c == "1" and c == newA[i]:
                newA[i] = "0"
            elif c == "1" and c != newA[i]:
                newA[i] = c
                c = ""
            if not(newA[i] == "1" and newA[i] == newB[i]): 
                newAB += str(int(newA[i]) + int(newB[i]))
            else:
                newAB += "0"
                c = "1"
        newAB += c if c else ""
        newAB = newAB[::-1]
        return newAB        