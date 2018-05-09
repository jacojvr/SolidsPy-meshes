# -*- coding: utf-8 -*-
"""
Generate input files for a finite element analysis in SolidsPy

@author: Nicolas Guarin-Zapata
"""
from __future__ import division, print_function
import numpy as np
import meshio
import solidspy.preprocesor as msh


def locate_pts_line(physical_line, points):
    """
    Find the nodes located on a physical line and their coordinates

    Parameters
    ----------
    physical_line : int
        Physical line identifier.
    points : array
        Array with the coordinates of the mesh.

    Returns
    -------
    nodes_line : list
        Number identifier for nodes on the physical line.
    line_x : array
        Array with the x coordinates for the nodes locates in the
        physical line.
    line_y : array
        Array with the y coordinates for the nodes locates in the
        physical line.
    """
    lines = cells["line"]
    phy_line = cell_data["line"]["gmsh:physical"]
    id_carga = [cont for cont in range(len(phy_line))
                if phy_line[cont] == physical_line]
    nodes_line = lines[id_carga]
    nodes_line = nodes_line.flatten()
    nodes_line = list(set(nodes_line))
    line_x = points[nodes_line][:, 0]
    line_y = points[nodes_line][:, 1]
    return nodes_line, line_x, line_y


# Read mesh file
archivo = "dam.msh"
points, cells, point_data, cell_data, field_data = meshio.read(archivo)

# Elements
nodes_array = msh.node_writer(points, point_data)
nf, els_array = msh.ele_writer(cells, cell_data, "triangle", 3, 3, 0, 0)


# Nodes
nodes_array = msh.boundary_conditions(cells, cell_data, 1, nodes_array, -1, -1)

# Loads
carga_mag = 40.0
nodes_line, x_load, y_load = locate_pts_line(2, points)
load_x = y_load - 40
load_y = 0.0
cargas = msh.loading(cells, cell_data, 2, load_x, load_y)

# Materials
materiales = np.array([[200000.0, 0.3]])

# Save files
np.savetxt("eles.txt", els_array, fmt="%d")
np.savetxt("loads.txt", cargas, fmt=("%d", "%.6f", "%.6f"))
np.savetxt("nodes.txt", nodes_array, fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
np.savetxt("mater.txt", materiales)
