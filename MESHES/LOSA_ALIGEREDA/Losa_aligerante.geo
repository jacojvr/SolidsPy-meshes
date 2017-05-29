lado_ele = 1.0;
rad = 0.5;
ancho = 6;
alto = 2;
L = ancho/3;

// Puntos
Point(1) = {0, 0, 0, lado_ele};
Point(2) = {ancho, 0, 0, lado_ele};
Point(3) = {ancho, alto, 0, lado_ele};
Point(4) = {0, alto, 0, lado_ele};
Point(5) = {1, alto/2, 0, lado_ele};
Point(6) = {3, alto/2, 0, lado_ele};
Point(7) = {5, alto/2, 0, lado_ele};
Point(8) = {1.5, alto/2, 0, lado_ele};
Point(9) = {0.5, alto/2, 0, lado_ele};
Point(10) = {3.5, alto/2, 0, lado_ele};
Point(11) = {2.5, alto/2, 0, lado_ele};
Point(12) = {5.5, alto/2, 0, lado_ele};
Point(13) = {4.5, alto/2, 0, lado_ele};

// Lineas
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Circle(5) = {8, 5, 9};
Circle(6) = {9, 5, 8};
Circle(7) = {10, 6, 11};
Circle(8) = {11, 6, 10};
Circle(9) = {12, 7, 13};
Circle(10) = {13, 7, 12};


// Superficie
Line Loop(1) = {3, 4, 1, 2};
Line Loop(2) = {5, 6};
Line Loop(3) = {7, 8};
Line Loop(4) = {9, 10};
Plane Surface(1) = {1, 2, 3, 4};


// Grupos fisicos
Physical Line(1) = {4, 2}; // Empotramiento
Physical Line(2) = {3};  // Carga
Physical Surface(3) = {1};
