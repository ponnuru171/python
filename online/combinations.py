from itertools import *
S, k = input().split()
for i in combinations(sorted(S),int(k)):
    print("".join(i))
"""from itertools import *
string, n = input().split()
for i in range(1,int(n)+1):
    data = ["".join(sorted(i)) for i in combinations(string,i)]
    data.sort()
    print("\n".join(data))"""