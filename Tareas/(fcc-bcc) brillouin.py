import numpy as np
import pyvista as pv

# vectores basados
b1, b2, b3 = 0.5 * (1 - 2 * np.eye(3))

# Dimensiones de la malla (2n+1)^3
n = 1

# Construcción de malla
I, J, K = np.mgrid[-n:n+1, -n:n+1, -n:n+1]

# Combinación lineal increible
pts = I[..., None] * b1 + J[..., None] * b2 + K[..., None] * b3
pts = pts.reshape(-1,3) # Al poner -1, numpy infiere la cantidad de puntos (2n+1)^3

# Ordenamiento y eliminacion de puntos innecesarios
mag = np.linalg.norm(pts, axis=1)
order = np.argsort(mag)
pts_ord = pts[order][1:15] # Tomar los primeros 14 puntos (excluyendo el origen)

# Crear plotter
plotter = pv.Plotter()

hexagonal_planes = len(pts_ord) - 6

# Crear los planos
#Trucazo increible usando el parametro c_res
for i in range(hexagonal_planes): # Solo los planos hexagonales
    plane = pv.Disc(center=pts_ord[i,:]/2,      # punto central del plano
                     normal=pts_ord[i,:],   # vector normal al plano
                     inner=0.0, outer=0.355,   # tamaño del plano en direcciones radiales
                     r_res=1, c_res=6)  # densidad de subdivisión
    plotter.add_mesh(plane, color="aquamarine", opacity=0.5, show_edges=True)

for i in range(hexagonal_planes, len(pts_ord)): # Solo los planos faltantes, osea los mas lejanos y cuadrados
    plane = pv.Disc(center=pts_ord[i,:]/2,      # punto central del plano
                     normal=pts_ord[i,:],   # vector normal al plano
                     inner=0.0, outer=0.25,   # tamaño del plano en direcciones radiales
                     r_res=1, c_res=4)  # densidad de subdivisión
    plotter.add_mesh(plane, color="aquamarine", opacity=0.5, show_edges=True)

# Crear plotter# Mostrar
plotter.show()