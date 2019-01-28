import matplotlib.pyplot as plt
import numpy as np

xAxis = np.array([])
for i in range(0, 151, 10):
    if i % 100 == 20 or i % 100 == 0:
        xAxis = np.append(xAxis, i)
    xAxis = np.append(xAxis, i)

# set V to 10, which will be called V_in
V = np.array([])
for i in range(len(xAxis)):
    V = np.append(V, 10)

D = np.array([-10,10,10,10,-10,-10,-10,-10,-10,-10,-10,-10,-10,10,10,10,-10,-10,-10,-10])

I = np.array([5,5,3.5,2,2,2+3/8,2+6/8,2+9/8,2+12/8,2+15/8,2+18/8,2+21/8,5,5,3.5,2,2,2+3/8,2+6/8,2+9/8])

plt.plot(xAxis, V, label='V_motor')
plt.plot(xAxis, D, label='Duty ratio')
plt.plot(xAxis, I, label='I_motor')
plt.legend()
plt.xticks([0,20,100,120])
plt.yticks([-10,10], ['-V_in', 'V_in'])
plt.xlabel('time (ms)')
plt.title('Speed control of DC motor')
plt.show()
