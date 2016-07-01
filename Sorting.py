v = int(raw_input())
lenOfArr = int(raw_input())
arr = map(int,raw_input().split())
for i in xrange(lenOfArr):
    if v == arr[i]: print i
