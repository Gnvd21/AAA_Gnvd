import matplotlib.pyplot as plt, mpld3

x = 10
y = 3

#x divided by y
print(x/y)
#x floor divided by y (division exclusing remainder)
print(x//y)
#x times y
print(x*y)
#x raised to the power of y
print(x**y)


plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
mpld3.show()
