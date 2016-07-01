from math import *
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in xrange(int(raw_input())):
    k = raw_input().strip().split()
    a = ceil(sqrt(int(k[0])))
    b = floor(sqrt(int(k[1])))
    print int(b-a+1)
