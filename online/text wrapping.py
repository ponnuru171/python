import textwrap
def wrap(x,z):
    return textwrap.wrap(x,z)
def fill(x,z):
    return textwrap.fill(x,z)
if __name__ == "__main__":
    x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    z=4
    result=wrap(x,z)
    result1=fill(x,z)
    print(result)
    print(result1)