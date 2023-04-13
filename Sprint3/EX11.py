f = open('arquivo_texto.txt', 'r')
text = ''

for x in f.readlines():
    text += x

print(text)
