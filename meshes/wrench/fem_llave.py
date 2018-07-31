"""
Solve for a wrench with a force applied in one extreme

@author: Nicolas Guarin-Zapata
@date: May 24, 2017
"""
from __future__ import division, print_function
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import solidspy.preprocesor as pre
import solidspy.postprocesor as pos
import solidspy.assemutil as ass
import solidspy.solutil as sol

start_time = datetime.now()

#%% PRE-PROCESSING
nodes, mats, elements, loads = pre.readin(folder="./")
DME , IBC , neq = ass.DME(nodes, elements)
print("Number of nodes: {}".format(nodes.shape[0]))
print("Number of elements: {}".format(elements.shape[0]))
print("Number of equations: {}".format(neq))

#%% SYSTEM ASSEMBLY
KG = ass.assembler(elements, mats, nodes, neq, DME)
RHSG = ass.loadasem(loads, IBC, neq)

#%% SYSTEM SOLUTION
UG = sol.static_sol(KG, RHSG)
end_time = datetime.now()
print('Duration for system solution: {}'.format(end_time - start_time))

#%% POST-PROCESSING
start_time = datetime.now()
UC = pos.complete_disp(IBC, nodes, UG)
E_nodes, S_nodes = pos.strain_nodes(nodes , elements, mats, UC)
#pos.fields_plot(elements, nodes, UC)
umag = np.linalg.norm(UC, axis=1)
mises = np.sqrt(S_nodes[:, 0]**2 - S_nodes[:, 0]*S_nodes[:, 1] +
                S_nodes[:, 1]**2 + 3*S_nodes[:, 2]**2)
tri = pos.mesh2tri(nodes, elements)
plt.figure(figsize=(10, 5))
plt.subplot(121)
pos.tri_plot(tri, umag, title=r"$\Vert \mathbf{u}\Vert$ (mm)", levels=12)
plt.subplot(122)
pos.tri_plot(tri, mises, title=r"von Mises Stress (MPa)", levels=12)
plt.savefig("wrench.png", dpi=300)
end_time = datetime.now()
print('Duration for post processing: {}'.format(end_time - start_time))
print('Analysis terminated successfully!')
plt.show()
