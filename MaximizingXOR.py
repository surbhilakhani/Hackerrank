def  maxXor( l,  r):
    a = []
    k = min(l,r)
    r = max(l,r)
    for i in xrange(k,r+1):
        for j in xrange(k,r+1):
            a.append(i^j)
    return max(a)

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
