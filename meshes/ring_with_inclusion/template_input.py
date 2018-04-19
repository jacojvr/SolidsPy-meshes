# -*- coding: utf-8 -*-
"""
Created on Fri May 05 13:30:46 2017

@author: Nicolas Guarin-Zapata
@date: Mayo 5, 2017
"""
from __future__ import division, print_function
import meshio
import numpy as np 


points, cells, point_data, cell_data, field_data = \
    meshio.read("Cilindro_inclusion.msh")


# Datos elementales
eles = cells["quad"]
els_array = np.zeros([eles.shape[0], 7], dtype=int)
els_array[:, 0] = range(eles.shape[0])
els_array[:, 1] = 1
els_array[:, 3::] = eles

# Nodos
nodes_array = np.zeros([points.shape[0], 5])
nodes_array[:, 0] = range(points.shape[0])
nodes_array[:, 1:3] = points[:, :2]

# Fronteras
lines = cells["line"]
bounds = cell_data["line"]["physical"]

# Cargas


# Condiciones de frontera


## Materiales
mater_array = np.array([[70e9, 0.35]])  # MPa

np.savetxt("eles.txt", els_array, fmt="%d")
np.savetxt("nodes.txt", nodes_array, fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
np.savetxt("loads.txt", loads_array, fmt=("%d", "%.6f", "%.6f"))
np.savetxt("mater.txt", mater_array, fmt="%.6f")