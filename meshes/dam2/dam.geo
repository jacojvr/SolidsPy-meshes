/*

*/
ndiv_hor = 10;
ndiv_vert = 10;
ndiv_base = 20;

// Points
Point(1) = {-5, 50, 0, 1.0};
Point(2) = {5, 50, 0, 1.0};
Point(3) = {5, 40, 0, 1.0};
Point(4) = {-5, 40, 0, 1.0};
Point(5) = {-25, 0, 0, 1.0};
Point(6) = {25, 0, 0, 1.0};

// Lines
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Line(5) = {4, 5};
Line(6) = {5, 6};
Line(7) = {6, 3};

// Surface
Line Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {-1};
Line Loop(2) = {5, 6, 7, 3};
Plane Surface(2) = {2};

// Physical groups
Physical Line(1) = {6};
Physical Line(2) = {5};
Physical Surface(3) = {2, 1};

// Meshing parameters
Transfinite Line{1, 3, 6} = ndiv_hor;
Transfinite Line{2, 4} = ndiv_vert;
Transfinite Line{5, 7} = ndiv_base;
Transfinite Surface{1};
Transfinite Surface{2};


