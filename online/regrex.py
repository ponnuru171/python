import re
T = int(input())
for i in range(0, T):
    regex_1 = input()
    try:
        regex = re.compile(regex_1)
    except re.error:
        print(False)
    else:
        print(True)