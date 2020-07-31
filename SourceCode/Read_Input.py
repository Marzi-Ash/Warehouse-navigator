import numpy as np

def Read_Input (FileName):
	data_list = [i.strip('\n').split('\t') for i in open(FileName)]
	columns = len(data_list[2])
	rows = len(data_list)
	InputMat = np.zeros((rows-1,columns))
	# convert input as a list to matrix
	for row in xrange(1,rows):
		data_list[row] = map(float, data_list[row])
		InputMat[row-1,:] = data_list[row]
	return InputMat
