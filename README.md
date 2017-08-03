# Meshes to conduct 2D-Finite Element Analysis with Python

![Structured mesh with traingular elements.](./docs/img/llave.png)


This _repo_ contains several finite element meshes, most of them created with [Gmsh](http://gmsh.info/), and to be analyzed with the python code
[SOLIDSPy](https://github.com/AppliedMechanics-EAFIT/SolidsPy).

The input to the FEM code is given in terms of text files defining nodal data (coordinates and boundary conditions), element data (connectivities and material profile), material property data (elastic constants) and point load data (nodes and load magnitude).

The folder `docs/` contains a step-by-step tutorial showing how to build a mesh using [Gmsh](http://gmsh.info/) and a scripting tool based on [`meshio`](https://github.com/nschloe/meshio) useful for converting the mesh into text files.

The folder `meshes/` contains several models. Each model consists of the .geo and .msh fils, the pre-processing subroutine based on [`meshio`](https://github.com/nschloe/meshio) and the resulting text files. 


## Authors
- [Juan Gomez](http://www.eafit.edu.co/docentes-investigadores/Paginas/juan-gomez.aspx),
    Professor at Universidad EAFIT.
- [Nicolás Guarín-Zapata](https://github.com/nicoguaro),
    Researcher at the Applied Mechanics Group at Universidad EAFIT.
