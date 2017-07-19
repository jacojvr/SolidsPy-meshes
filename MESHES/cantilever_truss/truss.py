# -*- coding: utf-8 -*-
"""

"""
from __future__ import division, print_function
import numpy as np
from datetime import datetime
import solidspy.preprocesor as pre
import solidspy.postprocesor as pos
import solidspy.assemutil as ass
import solidspy.solutil as sol


start_time = datetime.now()

#%% PRE-PROCESSING
nodes, mats, elements, loads = pre.readin()
DME , IBC , neq = ass.DME(nodes, elements)
print("Number of nodes: {}".format(nodes.shape[0]))
print("Number of elements: {}".format(elements.shape[0]))
print("Number of equations: {}".format(neq))

#%% SYSTEM ASSEMBLY
KG = ass.assembler(elements, mats, nodes, neq, DME, sparse=False)
RHSG = ass.loadasem(loads, IBC, neq)

##%% SYSTEM SOLUTION
UG = sol.static_sol(KG, RHSG)
if not(np.allclose(KG.dot(UG)/KG.max(), RHSG/KG.max())):
    print("The system is not in equilibrium!")
end_time = datetime.now()
print('Duration for system solution: {}'.format(end_time - start_time))

#%% POST-PROCESSING
start_time = datetime.now()
UC = pos.complete_disp(IBC, nodes, UG)
pos.fields_plot(elements, nodes, UC)
end_time = datetime.now()
print('Duration for post processing: {}'.format(end_time - start_time))
print('Analysis terminated successfully!')
