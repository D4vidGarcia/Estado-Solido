## Requerimientos

Este proyecto se ejecutó en un entorno que incluía las siguientes librerías de Python  
*(no todas son estrictamente necesarias para correr el código):*

- numpy  
- scipy  
- matplotlib  
- ipykernel  
- ipywidgets  
- pyvista[jupyter]  
- trame  
- trame-client  
- trame-vtk  
- trame-vuetify

En Google Colab solo es necesario **descomentar** la primera línea de los notebooks, ya que allí se encuentra el comando para instalar automáticamente las dependencias faltantes:

```python
# Descomentar la siguiente línea si se está utilizando Google Colab
# !pip install --quiet pyvista[jupyter] trame trame-client trame-vtk trame-vuetify
