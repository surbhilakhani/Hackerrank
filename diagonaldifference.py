import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
sum1 = 0
sum2 = 0
for i in xrange(len(a)):
    sum1 += a[i][i]
a=a[::-1]
for i in xrange(len(a)):
    sum2 += a[i][i]
print abs(sum1-(sum2))
