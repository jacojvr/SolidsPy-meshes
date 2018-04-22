# -*- coding: utf-8 -*-
"""
Genera archivos de entrada para el programa de elementos finitos
FEM_iso para una losa con aligerante.

@author: Nicolas Guarin-Zapata
@date: Mayo 22, 2017
"""
from __future__ import division, print_function
import meshio
import numpy as np 


points, cells, point_data, cell_data, field_data = \
    meshio.read("voided_slab.msh")

# Datos elementales
eles = cells["triangle"]
els_array = np.zeros([eles.shape[0], 6], dtype=int)
els_array[:, 0] = range(eles.shape[0])
els_array[:, 1] = 3
els_array[:, 3::] = eles

# Nodos
nodes_array = np.zeros([points.shape[0], 5])
nodes_array[:, 0] = range(points.shape[0])
nodes_array[:, 1:3] = points[:, :2]

# Fronteras
lines = cells["line"]
bounds = cell_data["line"]["gmsh:physical"]
nbounds = len(bounds)

# Cargas
id_cargas = [cont for cont in range(nbounds) if bounds[cont] == 2]
nloads = len(id_cargas)
load = -10e8 # N/m
loads_array = np.zeros((nloads, 3))
loads_array[:, 0] = id_cargas
loads_array[:, 1] = 0
loads_array[:, 2] = load

# Condiciones de frontera
id_lat = [cont for cont in range(nbounds) if bounds[cont] == 1]
nodes_lat = lines[id_lat]
nodes_lat = nodes_lat.flatten()
nodes_array[nodes_lat, 3:] = -1

#  Materiales
mater_array = np.array([[70e9, 0.20]])

# Generar archivos
np.savetxt("eles.txt", els_array, fmt="%d")
np.savetxt("nodes.txt", nodes_array,
           fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
np.savetxt("loads.txt", loads_array, fmt=("%d", "%.6f", "%.6f"))
np.savetxt("mater.txt", mater_array, fmt="%.6f")
