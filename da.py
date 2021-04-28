import matplotlib.pyplot as plt
plt.plot(x,y, linewidth = 3, color = 'red', linestyle = 'dashed')
plt.bar(x,y,width = 0.9, color ='red' )
plt.title("str1")
plt.xlabel("str2")
plt.ylabel("str3")
plt.legend()
plt.show()

plt.xlabels = ['Jan','Feb', 'Mar', 'Apr', 'May']  #multiple labels
plt.xticks(x,xlabels,rotation = 45)

M = [25,30,21,27,53]
F = [27,25,21,30,33]
x = np.arange(len(M))
plt.bar(x,M, width = 0.2)
plt.bar(x+0.2,F, width = 0.2)
plt.grid(True, color = 'red')
plt.show()


#NUMPY
import numpy as np
x = np.arange(16)
y = x**2
plt.plot(x,y)
plt.show()