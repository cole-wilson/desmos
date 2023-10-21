colors = {}
f = open("./obj.mtl").read().split("\n")
key = None
for line in f:
    if line.startswith("newmtl "):
        key = line.lstrip("newmtl ")
    if line.startswith("Kd"):
        line = line.split()
        rgbs = list(map(lambda i: round(float(i)*255), line[1:]))
        colors[key] = rgbs


color_list = []

d = open("./tinker.obj").read().split("\n")
vertices = []
faces = []
for line in d:
    if line.startswith("v "):
        vertices.append(list(map(float,line.split()[1:])))
    elif line.startswith("f "):
        color_list.append(colors[key])
        faces.append(list(map(int,line.split()[1:])))
    elif line.startswith("usemtl "):
        key = line.lstrip("usemtl ")


B_x, B_y, B_z = list(zip(*vertices))
print(f"B_x={list(B_x)}")
print(f"B_y={list(B_y)}")
print(f"B_z={list(B_z)}")

F_a, F_b, F_c = list(zip(*faces))
print(f"F_a={list(F_a)}")
print(f"F_b={list(F_b)}")
print(f"F_c={list(F_c)}")

R, G, B = list(zip(*color_list))
print(f"R={list(R)}")
print(f"G={list(G)}")
print(f"B={list(B)}")

print("\n"*5)
print(len(vertices), "vertices,", len(faces), "triangles")

triangles = []


# for point_refs in faces:
#     triangles.append(vertices[point_refs[0]-1])
#     triangles.append(vertices[point_refs[1]-1])
#     triangles.append(vertices[point_refs[2]-1])
#     triangles.append(vertices[point_refs[0]-1])
#     # print(triangles[-4:])

# faces = list(map(list, zip(*triangles)))
# color_list = list(map(list, zip(*color_list)))

# # faces = list(map(list, zip(*faces)))


# print("X_{box} =", faces[0])
# print("Y_{box} =", faces[1])
# print("Z_{box} =", faces[2])
# print("R =", color_list[0])
# print("G =", color_list[1])
# print("B =", color_list[2])
