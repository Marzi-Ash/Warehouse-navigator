import numpy as np

def Exact_Shelf (InputMat):
	columns = int(max(InputMat[:,2]))+1
	rows = int(max(InputMat[:,1]))+1
	LocMat = np.zeros((rows,columns))
	for product in xrange(0, len(InputMat)):
		# set the element of matirx to 1 if there exist a shelf on that location
		LocMat[int(InputMat[product][1]),int(InputMat[product][2])] = 1
		#locMat=LocMat.T
	return np.rot90(LocMat)
