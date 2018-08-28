
# coding: utf-8

# In[7]:


f = open('dic.txt', 'r')
for line in f:
 print(line)
f.close()


# In[46]:


f = open('dic2.txt', 'r')
z = open("article.txt", encoding="utf8")
r=0
for line in f:
    lines = [line.rstrip('\n') for line in open('dic2.txt')]
    for s in z:
        i = s.find(line)  
        if i > -1:
         r += 1
        else:
         i = s.find(line)  
    print(line, r)
    
f.close()
z.close()


# In[12]:


z = open("article.txt", encoding="utf8")
n = 0
for line in z:
 i = line.find(line)    
 if i > -1:
  n += 1
 return(n)
 
print(line, n)
f.close()


# In[136]:


f = open('dic2.txt').read().splitlines()
z = open("article.txt", encoding="utf8")


for line in f:
             
    for s in z:
        r=0
        i = s.find(line)   
        if i > -1:
         r += 1
    print(line, r)

  

z.close()
f.close()


# In[12]:


f = open('dic2.txt').read().splitlines()

for line in f:
    r=0
    z = open('article.txt', encoding="utf8")        
    for s in z:
        i = s.find(line) 
        if i > -1:
         r += 1 
    print(line, r)
    z.close()

