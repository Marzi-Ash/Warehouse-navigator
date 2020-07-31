from Read_Input import Read_Input
from Exact_Shelf import Exact_Shelf
from Read_File import Read_File
import numpy as np

InputMat = Read_Input('qvBox-warehouse-data-s19-v01.txt')
LocMat = Exact_Shelf(InputMat)
DistMat = np.load("DistMat.npy")
# InputFile is from 0 to 99 for a file with 100 orders
InputFile, InputFlag = Read_File('qvBox-warehouse-orders-list-part01.txt')
