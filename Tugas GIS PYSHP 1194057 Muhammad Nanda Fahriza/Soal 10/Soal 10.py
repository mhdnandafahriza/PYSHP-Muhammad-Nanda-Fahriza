import shapefile
print(1194025 % 8)

w = shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType


w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("Muhammad", "Satu")
w.record("Nanda", "Dua")
w.record("Fahriza", "Tiga")
w.record("Kelas", "Empat")
w.record("B", "Lima")

w.poly([[[2, 1], [8, 1], [5, 5], [2, 1]]])
w.poly([[[9, 1], [15, 1], [12, 5], [9, 1]]])
w.poly([[[16, 1], [22, 1], [19, 5], [16, 1]]])
w.poly([[[23, 1], [29, 1], [26, 5], [23, 1]]])
w.poly([[[30, 1], [36, 1], [33, 5], [30, 1]]])

