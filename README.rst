Meshes to conduct 2D-Finite Element Analysis with Python
========================================================

.. figure:: ./img/spanner.svg
   :alt: Mesh for a spanner with triangular elements.
   :width: 800 px


This *repo* contains several files with geometry and meshes for
finite element analyses, most of them created were created
with `Gmsh <http://gmsh.info/>`__. They were mainly created
to be analyzed using
`SolidsPy <https://github.com/AppliedMechanics-EAFIT/SolidsPy>`__.

The input to the FEM code is given in terms of text files defining nodal
data (coordinates and boundary conditions), element data (connectivities
and material profile), material property data (elastic constants) and
point load data (nodes and load magnitude). For tutorials on how to use
them consult `documentation of SolidsPy <http://solidspy.readthedocs.io/en/latest/tutorial.html>`__.


The folder ``meshes/`` contains several models. Each model consists of
the .geo and .msh filEs, the pre-processing Python scripts that use
`meshio <https://github.com/nschloe/meshio>`__  and the resulting
text files.

Authors
-------

-  `Juan Gomez <http://www.eafit.edu.co/docentes-investigadores/Paginas/juan-gomez.aspx>`__,
   Professor at Universidad EAFIT.
-  `Nicolás Guarín-Zapata <https://github.com/nicoguaro>`__, Researcher
   at the Applied Mechanics Group at Universidad EAFIT.
