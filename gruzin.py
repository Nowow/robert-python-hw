
gruztext = open('gruzin.txt', 'r', encoding='utf-8')
vec = {}
for line in gruztext:
    cash = line.replace('\t', '').split(sep=' ')
    vec.update({cash[0]:cash[2]})
#print(vec)
#print(vec.keys())
#stin = ['asdasd']
gruztext.close()
gruzstih = open('gruzstih.txt', 'r', encoding='utf-8').read()
#print(gruzstih)

def gruztranslit(text = gruzstih):
    perevod = ''
    for char in text:
        if char in list(vec.keys()):
            char = vec[char]
            perevod = perevod + char
        else:
            perevod = perevod + char
    return perevod
print(gruztranslit())
#print(gruzstih)
#print(perevod)
#print(len(list(vec.keys())))
