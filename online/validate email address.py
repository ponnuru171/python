import re
import email.utils
a = int(input())
pat = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
for i in range(0, a):
    arran = email.utils.parseaddr(input())
    if re.search(pat, arran[1]):
        print(email.utils.formataddr(arran))