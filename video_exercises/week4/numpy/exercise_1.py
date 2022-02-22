import numpy as np

a = np.arange(10, 30).reshape(4, 5)
print(a)


red = a[0, 1:4]
yellow = a[0,0]
green = a[0:3, 2]
turquise = a[0:4, 1:4:2]
blue = a[0:3:2, 4]

#print(red, yellow, green,'\nturquise:\n',turquise,'\n blue:\n', blue )


data = np.arange(1,101).reshape(10,10)