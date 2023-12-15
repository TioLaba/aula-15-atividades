def tabuada(x):
    tabuada = []
    for i in range(1, 11):
        tabuada.append(str(x) + ' X ' + str(i) + ' = ' + str(x*i))
        return tabuada

for x in tabuada(1):
    print(x)