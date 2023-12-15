def media(valores):
    soma = 0
    for i in range(0, len(valores)):
        soma += valores[i]
    return soma/len(valores)

x = [2, 3, 4, 5]
print('a media de ', end='')
for valor in x:
    print(f' {valor}', end='')
print(' é {:.0f}'.format(media(x)))