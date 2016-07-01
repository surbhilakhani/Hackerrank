result = " " 
computing = {} 
listA = [] 
listB = [] 
firstline = raw_input ()     
N=int(firstline.split(" ")[0])
Q=int(firstline.split(" ")[1]) 
A = raw_input () 
B = raw_input () 

for i in range (N): 
      listA.append (A [N-1- i]) 
      listB.append (B [N-1- i]) 
sum = long (A [:: - 1], 2) + long (B [:: - 1], 2) 

for i in range (Q): 
      line = raw_input () 
      resultStr = line.split (" ") 
      NO = int (resultStr [1] ) 
      if resultStr [0] [4] == 'a' and resultStr [2] == listA [NO]: 
          listA [NO] = resultStr [2 ] 
          if resultStr [2] == '1': 
              sum = sum + (1 << NO ) 
          else: 
              sum = sum - (1 << NO ) 
      if resultStr [0] [4 ] == 'b' and resultStr [2] == listB [NO]: 
          listB [NO] = resultStr [2 ] 
          if resultStr [2] == '1': 
              sum = sum + (1 << NO ) 
          else: 
              sum = sum - (1 << NO ) 
      if resultStr [0] [4] == 'c': 
           if (sum & (1 << NO)) == 0: 
              result += '1' 
           else: 
              result += '0' 
print result 
