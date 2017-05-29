# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:27:20 2017

@author: andreavalenciatamayo
"""
from __future__ import division, print_function
import meshio
import numpy as np 
#
points, cells, point_data, cell_data, field_data = \
    meshio.read("tarea_puente.msh")
    
# Datos de los elementos
#
eles = cells["triangle"]
els_array = np.zeros([eles.shape[0], 6], dtype=int)
els_array[:, 0] = range(eles.shape[0])              # Asigna numero de elemento
els_array[:, 1] = 3                                 # Asigna tipo de elemento
els_array[:, 3::] = eles                           # Asigna nudos de los elementos
#
# Datos de los nudos
#
nodes_array = np.zeros([points.shape[0], 5])
nodes_array[:, 0] = range(points.shape[0])          # Asigna numeros de nudos
nodes_array[:, 1:3] = points[:, :2]                 # Asigna coordenadas

# Fronteras
lines = cells["line"]
bounds = cell_data["line"]["physical"]   
           # Bounds contiene la infromacion de la linea fisica

 # Cargas
id_carga = [cont for cont in range(len(bounds)) if bounds[cont] == 1]
nodes_carga = lines[id_carga]
nodes_carga = nodes_carga.flatten()
nodes_carga = list(set(nodes_carga))
ncargas = len(nodes_carga)
carga_total = -1e6
cargas_array = np.zeros((ncargas,3))
cargas_array[:, 0] = nodes_carga
cargas_array[:, 1] =0        
cargas_array[:, 2] = carga_total*points[nodes_carga, 1]/ncargas

#Condiciones de frontera
id_frontera_lat = [cont for cont in range(len(bounds)) if bounds[cont] == 2]
nodes_frontera_lat = lines[id_frontera_lat]
nodes_frontera_lat = nodes_frontera_lat.flatten()
nodes_frontera_lat = list(set(nodes_frontera_lat))
nodes_array[nodes_frontera_lat, 3] = -1
id_frontera_abajo  = [cont for cont in range(len(bounds)) if bounds[cont] == 3]
nodes_frontera_abajo = lines[id_frontera_abajo]
nodes_frontera_abajo = nodes_frontera_abajo.flatten()
nodes_frontera_abajo = list(set(nodes_frontera_abajo))
nodes_array[nodes_frontera_abajo, 4] = -1

#
# Datos de los materiales
#
mater_array = np.array([[12e9, 0.15],
                        [2e9, 0.30]])
maters = cell_data["triangle"]["physical"]
els_array[:, 2] = [0 if mater == 4 else 1 for mater in maters]

#
# Escribe los archivos 
#
np.savetxt("eles.txt" , els_array   , fmt="%d")
np.savetxt("nodes.txt", nodes_array , fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
np.savetxt("mater.txt", mater_array , fmt="%.6f")
np.savetxt("loads.txt", cargas_array, fmt=("%d", "%.6f", "%.6f"))