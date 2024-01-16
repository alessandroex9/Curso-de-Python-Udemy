"""
count é um iterador sem fim
Ele é a mesma coisa do range
Só que count vc não precisa passar onde ele vai acabar
Já no range vc precisa passar onde vai acabar

count está no modulo (itertools)
"""
#importanto o count
from itertools import count

c1 = count(8, 8)
r1 = range(8, 100, 8)

print(next(c1))
print(next(c1))



for i in c1:
    if i > 100:
        break
    else:
        print(i)
        continue
    
for i in r1:
    print(i)