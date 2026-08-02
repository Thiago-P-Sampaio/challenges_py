class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        print(numRows)
        for i in range(1,numRows+1):
            row = []
            for a in range(1,i+1):
                num = 1
                if a == 1 or a == i:
                    row.append(num)
                else:
                    num = pascal_triangle[i-2][a-1] + pascal_triangle[i-2][a-2]
                    row.append(num)
                if a/i == 1:
                    pascal_triangle.append(row)
        return pascal_triangle


  
if __name__ == "__main__":
    solution = Solution()

    # Testes locais
    print(solution.generate(6))
                
