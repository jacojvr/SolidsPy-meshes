"""

"""
from __future__ import division
import meshio
import numpy as np 


points, cells, point_data, cell_data, field_data = \
    meshio.read("spanner.msh")


# Elements data
elements = cells["triangle"]
els_array = np.zeros([elements.shape[0], 6], dtype=int)
els_array[:, 0] = range(elements.shape[0])
els_array[:, 1] = 3
els_array[:, 3::] = elements

# Nodes data
nodes_array = np.zeros([points.shape[0], 5])
nodes_array[:, 0] = range(points.shape[0])
nodes_array[:, 1:3] = points[:, :2]


np.savetxt("eles.txt", els_array, fmt="%d")
np.savetxt("nodes.txt", nodes_array, fmt=("%d", "%.4f", "%.4f", "%d", "%d"))

