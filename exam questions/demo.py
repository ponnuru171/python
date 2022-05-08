#str='abcd'
def comb(str):
    return ''.join(str)
def permute(a,l,r):
    if l==r:
        print(str(a))
    else:
        for i in range(l,r+1):
            a[l],a[i] =a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] =a[i],a[l]
string='abcd'
n=len(string)
a=list(string)
permute(a,0,n-1)
