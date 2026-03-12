import numpy as np
def rotation_matrix_x(degrees):
 angle=np.radians(degrees)
 return np.array([[1, 0, 0],
[0, np.cos(angle), -np.sin(angle)],
 [0 ,np.sin(angle), np.cos(angle)]]
)

result=rotation_matrix_x(45)
print(result)
