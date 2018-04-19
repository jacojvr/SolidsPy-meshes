#################################################################
# Plots the energy norm of the error for a series of FE soltns. #
#                                                               #
#################################################################
"""
Perfomrs converegency analysis
for a series of meshes
"""
#
import numpy as np
import matplotlib.pyplot as plt
#
h  = np.zeros([4],dtype=np.float128)
En = np.zeros([4],dtype=np.float128)
Er = np.zeros([4],dtype=np.float128)
Nel = np.zeros([4],dtype=np.int)
#
# Define characteristic element size
# and number of elements
#
h[0]=1.0
h[1]=0.5
h[2]=0.25
h[3]=0.125
Nel[0] = 10
Nel[1] = 39
Nel[2] = 160
Nel[3] = 640
#
# Potential energy of the finite element solution
#
En[0] = -0.2856 
En[1] = -0.2884 
En[2] = -0.2891 
En[3] = -0.2893
#
# Compute the exact potential energy (using the most refined meshes)
#
Pi_ex = (En[2]*En[2]- En[3]*En[1])/(2.0*En[2]-En[3]-En[1])
#
for i in range(4):
    Er[i] = np.sqrt((Pi_ex-En[i])/Pi_ex)
#
plt.figure(1)
plt.plot(Nel, Er)
plt.xlabel('Number of elements')
plt.ylabel('[Uex-Ufe]/Uex')
plt.show()  
#
# Measure the convergency rate
#
plt.figure(2)
plt.plot(h, Er)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('log(h)')
plt.ylabel('log([Uex-Ufe]/[Uex])')
plt.show()
#
m = (np.log(Er[3])-np.log(Er[2]))/(np.log(h[3])-np.log(h[2]))
print('Exact potential energy =' , Pi_ex)
print('Normalized energy norm of the error=' , Er)


