import sys


n = int(raw_input().strip())
for i in xrange(1,n+1):
    for j in xrange(n-i):
        sys.stdout.write(' ')
    for k in xrange(i):
        sys.stdout.write('#')
    sys.stdout.write('\n')
