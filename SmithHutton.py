from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Physical Data 
	# Geometry. [meters]
L=1			 
			# deep
	# Reynolds
	# Boundary Conditions

# Numerica Data
	# Number of control volumes 
N=8
M=int(N/2)
	# Convergence Criteria 
delta= 1e-6
	# What else? 

# Mesh / Geometrical Discretization
	# Control Volume's geometry. Quadrilateral. Structured. Cartesian. 
dx=2*L/N 				 
dy=L/M					

	# Definition of the nodes and control volumes. Node centered. 
		# Horizontal position of the control volume's west face 
Xcv=np.zeros(N)
for i in range(N):
	Xcv[i]=-L+i*dx 

		# Horizontal position of the nodes 
Xp=np.zeros(N+2)
for i in range(1,N+1):
	Xp[i]=Xcv[i-1]+dx/2
Xp[0]=-L
Xp[N+1]=L

		# Vertical position of the control volume's down face
Ycv=np.zeros(M)
for i in range(M):
	Ycv[i]=i*dy

		# Vertical position of the nodes
Yp=np.zeros(M+2)
Yp[0]=0
Yp[M+1]=L
for i in range(1,M+1):
	Yp[i]=Ycv[i-1]+dy/2

# Inititial variable values 
	# Inner nodes. Matrix Definition
V=np.ones((M+2,N+2))
	# Boundary. Inflow.
for i in range(int(N/2+1)):
	V[0][i]= 1+ np.tanh (10*(2*Xp[i]+1))			
	# Boundary. Outflow. 
for i in range(int(N/2+1), N+1):
	V[0][i]= 0
	# Boundary. Left. 
for j in range (1,M+1):
	V[j][0]= 1- np.tanh (10)
	# Boundary. Right. 
for j in range (1,M+1):
	V[j][N+1]= 1- np.tanh (10)
	# Boundary. Top. 
for i in range(N+1):
	V[M+1][i]= 1- np.tanh (10)
	# Corners                      # No funciona!! 
V[0][0]= 1- np.tanh (10)
V[0][N+1]= 1- np.tanh (10)
V[M+1][0]= 1- np.tanh (10)
V[M+1][N+1]= 1- np.tanh (10)
print (V)


# Assign vertical and horizontal velocities 

# Mass fluxes 
me= d*ue*dy

# Discretization coefficients. UDS (AP=1)
Ae= De + max([-me,0])
Aw= Dw + max([-mw,0])
An= Dn + max([-mn,0])
As= Ds + max([-ms,0])

# Solver 











