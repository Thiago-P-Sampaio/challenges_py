# Challenge: Pascal_Triangle
# https://leetcode.com/problems/pascals-triangle/description/

pascal = []
# O triângulo de pascal é uma tabela infinita onde as bordas sempre serão "1s" e os números internos
# serão resultados das somas entre os dois últimos termos de cima, formando um triângulo equilátero

def pascal_triangle(rows):
    row = []
    for i in range(1,rows+1):     
        print(f"Linha de repetição: {i} ")
        for a in range(1,i+1):
            # NÚMERO 1 PARA INICIAR E FINALIZAR LINHA
            num = 1
            # VERIFICAR INICIO E FIM DE REPETIÇÃO POR LINHA
            if a == 1 or a == i:
                row.append(num)
            else:
                # Faz o cálculo considerando a soma dos dois últimos valores da última linha
                num = pascal[i-2][a-1] + pascal[i-2][a-2]
                # "I" controla a linha, e durante as repetições por linha ele se mantém o mesmo
                # Meu erro foi considerar "A" como parâmetro para linha anterior, mas o "A"
                #muda constantemente dentro desse ciclo
                row.append(num)
                print("="*30 + " Cálculo anterior Errado " + "="*30
      +"\n" + f"Linha da repetição:{i}"
      +"\n" + f"Repetição por Linha:{a}"
      +"\n" + f"Linha base(antecessora):{pascal[a-1]}"
      +"\n" + f"Valores para formar próximo elemento: { pascal[a-1][a-2]} + {pascal[a-1][a-3]} = { pascal[a-1][a-2] + pascal[a-1][a-3]}"
      +"\n\n"
      )
                print("="*30 + " Cálculo Certo " + "="*30   
      +"\n" + f"Linha da repetição:{i}"
      +"\n" + f"Repetição por Linha:{a}"
      +"\n" + f"Linha base(antecessora):{pascal[i-2]}"
      +"\n" + f"Valores para formar próximo elemento: { pascal[i-2][a-1]} + {pascal[i-2][a-2]} = { pascal[i-2][a-1] + pascal[i-2][a-2]}"
      +"\n\n"
      )
            if a == i: 
                pascal.append(row)
                print("-"*30 + " Linha formada " + "-"*30 + "\n" + f"{row}" + "\n" +"-"*60)
                row = []
    print(pascal)

pascal_triangle(5)




# print("="*30 + " Cálculo anterior Errado " + "="*30
#       +"\n" + f"Linha da repetição:{i}"
#       +"\n" + f"Linha base(antecessora):{pascal[a-1]}"
#       +"\n" + f"Valores para formar próximo elemento: { pascal[a-1][a-2]} + {pascal[a-1][a-3]} = { pascal[a-1][a-2] + pascal[a-1][a-3]}"
#       )



# print("="*30 + " Cálculo Certo " + "="*30
#       +"\n" + f"Linha da repetição:{i}"
#       +"\n" + f"Linha base(antecessora):{pascal[i-2]}"
#       +"\n" + f"Valores para formar próximo elemento: { pascal[i-2][a-1]} + {pascal[i-2][a-2]} = { pascal[i-2][a-1] + pascal[i-2][a-2]}"
#       )

                # print(f" Certo: {pascal[i-2]}  \t A = {a}  | { pascal[i-2][a-1]} + {pascal[i-2][a-2]}\n")
                # print(f" Errado: {pascal[a-1]}  \t A = {a}  | { pascal[a-1][a-2]} + {pascal[a-1][a-3]} \n")
