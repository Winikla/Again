
def stars (h):
    i ='*'
    j = 0
    while j <= h:
        print(i*j)
        j = j +1   
    
stars(5)
    
def backstars(j):    
    i ='*'
    while j >= 0 :
        print(i * j)
        j = j -1   
        
backstars(5)


def restars(k):    
    i ='*'
    g=' '
    h = 0
    j = k 
    while h <= k : 
        print((g * j) + (i * h))
        j = j - 1 
        h = h + 1  
         
restars(5)



def backrestars(k):    
    i ='*'
    g=' '
    h = 0
    j = k 
    while h <= k : 
        print((g * h) + (i * j))
        j = j - 1 
        h = h + 1  
         
backrestars(5)


