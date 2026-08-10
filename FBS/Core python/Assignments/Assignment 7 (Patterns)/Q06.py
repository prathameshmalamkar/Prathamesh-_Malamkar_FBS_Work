### Q6. Print following patterns:
## f.  
# 1 2 3 4 5 
# 2     5 
# 3   5 
# 4 5 
# 5 

## starts:

for i in range (1, 6):
    
    for j in range (i, 6):
        
        if(j==i or i==1 or j==5 ):
            print(j,  end = " ")
            
        else:
            print(" ",end = " ")
            
    print()
