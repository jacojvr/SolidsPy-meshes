# -*- coding: utf-8 -*-
"""
Create input files for the FEM program Solidspy for the brazilian
test using 2 symmetries in the model.

@author: Nicolas Guarin-Zapata
@date: March 2010
"""
import meshio
import numpy as np 



mesh = meshio.read("brazilian_test.msh")
points = mesh.points
cells = mesh.cells
point_data = mesh.point_data
cell_data = mesh.cell_data
field_data = mesh.field_data

# Element data
eles = cells["triangle"]
els_array = np.zeros([eles.shape[0], 6], dtype=int)
els_array[:, 0] = range(eles.shape[0])
els_array[:, 1] = 3
els_array[:, 3::] = eles

# Nodes
nodes_array = np.zeros([points.shape[0], 5])
nodes_array[:, 0] = range(points.shape[0])
nodes_array[:, 1:3] = points[:, :2]

# Boundaries
lines = cells["line"]
bounds = cell_data["line"]["gmsh:physical"]
nbounds = len(bounds)

# Loads
id_cargas = cells["vertex"]
nloads = len(id_cargas)
load = -10e8 # N/m
loads_array = np.zeros((nloads, 3))
loads_array[:, 0] = id_cargas
loads_array[:, 1] = 0
loads_array[:, 2] = load

# Boundary conditions
id_izq = [cont for cont in range(nbounds) if bounds[cont] == 1]
id_inf = [cont for cont in range(nbounds) if bounds[cont] == 2]
nodes_izq = lines[id_izq]
nodes_izq = nodes_izq.flatten()
nodes_inf = lines[id_inf]
nodes_inf = nodes_inf.flatten()
nodes_array[nodes_izq, 3] = -1
nodes_array[nodes_inf, 4] = -1

#  Materiales
mater_array = np.array([[186e9, 0.29],
                        [70e9, 0.35]])
maters = cell_data["triangle"]["gmsh:physical"]
els_array[:, 2]  = [0 if mater == 4 else 1 for mater in maters]

# Generar archivos
np.savetxt("eles.txt", els_array, fmt="%d")
np.savetxt("nodes.txt", nodes_array,
           fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
np.savetxt("loads.txt", loads_array, fmt=("%d", "%.6f", "%.6f"))
np.savetxt("mater.txt", mater_array, fmt="%.6f")
