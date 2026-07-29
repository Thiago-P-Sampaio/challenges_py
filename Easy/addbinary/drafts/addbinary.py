def addbinary(a,b):
    newA, newB, newAB, c,difference = list(a), list(b), "", "", abs(len(a)-len(b))
    print(difference)
    if len(newA) > len(newB):
        while difference > 0:
            newB.insert(0, "0")
            difference -= 1
    elif len(newB) > len(newA):
        while difference > 0:
            newA.insert(0, "0")
            difference -=1
    print(f"NEWA={newA} \t")
    print(f"NEWB={newB}")
    for i in range(len(newA)-1, -1, -1):
        if c == "1" and c == newA[i]:
            newA[i] = "0"
            print(f"{i}º \t c={c} \t newA ={newA[i]} \t newB={newB[i]} \n ")
        elif c == "1" and c != newA[i]:
            newA[i] = c
            c = ""
            print(f"{i}º \t c={c} \t newA ={newA[i]} \t newB={newB[i]} \n ")
        if not(newA[i] == "1" and newA[i] == newB[i]): 
            newAB += str(int(newA[i]) + int(newB[i]))
            print(f"{i}º \t c={c} \t newA ={newA[i]} \t newB={newB[i]} \t soma={int(newA[i]) + int(newB[i])} \t newAB ={newAB} \n")
        else:
            newAB += "0"
            c = "1"
            print(f"{i}º \t c={c} \t newA ={newA[i]} \t newB={newB[i]} \t newAB ={newAB} \n")
    newAB += c if c else ""
    newAB = newAB[::-1]
    print(f" \n\n Resultado final de c={c} \n\n")
    print(newAB)




addbinary("111","1010")

## +5 horas nesse exercício kkkk