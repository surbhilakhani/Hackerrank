import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    c = 0
    for i in xrange(len(a)):
        if a[i]<1:c+=1
    if c>=k: print 'NO'
    else: print 'YES'
