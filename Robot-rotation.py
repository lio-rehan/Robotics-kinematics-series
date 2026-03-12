import numpy as np
def rotation_matrix_x(degrees):
 angle=np.radians(degrees)
 return np.array([[1, 0, 0],
[0, np.cos(angle), -np.sin(angle)],
 [0 ,np.sin(angle), np.cos(angle)]]
)
def rotation_matrix_y(degrees):
    angle=np.radians(degrees)
    return np.array([[np.cos(angle),0 ,np.sin(angle)],
                     [0 , 1 , 0],
                     [np.sin(angle), 0, np.cos(angle)]

                     ])

def rotation_matrix_z(degrees):
 angle=np.radians(degrees)
 return np.array([
     [np.cos(angle),-np.sin(angle),0],
     [np.sin(angle),np.cos(angle),0],
     [0 ,0 ,1]

 ])
result_x=rotation_matrix_x(45)
result_y=rotation_matrix_y(60)
result_z=rotation_matrix_z(30)
print(result_x)
print(result_y)
print(result_z)