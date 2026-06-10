n = int(input())
count = 0
faces = {"Tetrahedron":4, "Cube":6, "Octahedron":8, "Dodecahedron":12, "Icosahedron":20}


for _ in range(n):
    polyhedron = input()
    count += faces[polyhedron]

print(count)