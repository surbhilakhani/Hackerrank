string = list(raw_input())
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
a = []
string.sort()
j = 0
for i in xrange(len(string)-1):
    if string[i]!=string[i+1]:
        a.append(i-j)
        j = i
count = 0
for k in xrange(len(a)):
    if a[k]%2!=0: count += 1
if count < 2: found = True
    
    
if not found:
    print("NO")
else:
    print("YES")
