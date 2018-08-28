
# coding: utf-8

if = open('dic2.txt').read().splitlines()

for line in f:
    r=0
    z = open('article.txt', encoding="utf8")        
    for s in z:
        i = s.find(line) 
        if i > -1:
         r += 1 
    print(line, r)
    z.close()

