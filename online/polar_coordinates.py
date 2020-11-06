from cmath import sqrt,phase
a=complex(input())
print(sqrt(pow(a.real,2)+pow(a.imag,2)).real)
print(phase(complex(a.real,a.imag)))
