l=[2,3,8,6,3,9,0,88]
print l

for pos in range(len(l)):
    
    smallest=pos
    for i in range(pos,len(l)):
        
        if l[i]<l[smallest]:
            smallest=i
            
    l[smallest],l[pos]=l[pos],l[smallest]

    print l

    raw_input()
    
