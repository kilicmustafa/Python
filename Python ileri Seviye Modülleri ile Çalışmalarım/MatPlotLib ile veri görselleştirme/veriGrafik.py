import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1 ,6)
y = np.arange(2 ,11 ,2)

fig = plt.figure()


axes1 = fig.add_axes([0.1 ,0.1 ,0.6 ,0.6] )

axes2 = fig.add_axes([0.3 ,0.4 ,.3 ,.3])

axes1.plot(x,y,"red")


axes2.plot(x ,y ,"blue")
plt.show()