import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length, s = 0, re.sub(r"[^\w\s]", "", s).strip()
        s = s.split()
        s.reverse()
        print(s)
        length = len(s[0])
        return length


if __name__ == "__main__":
    solution = Solution()

    # Testes locais
    print(solution.lengthOfLastWord("Olá tudo bem? como você está?"))