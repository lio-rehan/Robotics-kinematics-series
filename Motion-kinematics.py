import numpy as np#configure your rotation matrix
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
values=input("Enter 3 values seperated by spaces:").split()
effector_pos=np.array([[float(val)] for val in values])

values=input("Enter 3 values seperated by spaces:").split()
motion_matrix=np.array([[float(val)] for val in values])
#enter a variable A,for the desired rotation and for  B, the end effector
A=rotation_matrix_z(50)
B=effector_pos
End_position=np.matmul(A,B)

Final_pos=End_position + motion_matrix
print(Final_pos)