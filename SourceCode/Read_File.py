import numpy as np

def Read_File(FileName):
    data_list = [i.strip('\n').split('\t') for i in open(FileName)]
    rows = len(data_list)
    columns = max(len(data_list[i]) for i in xrange(0,rows))

    InputFile = np.zeros((rows,columns))
    InputFlag = np.zeros((1,rows))
    for row in xrange(0,rows):
        for i in xrange(0,columns):
            if data_list[row][i] == '':
                data_list[row][i] = 0
            elif data_list[row][i] == '\r':
                data_list[row][i] = 0
        data_list[row] = map(int, data_list[row])
        n = data_list[row].count(0)
        del data_list[row][-n:]
        #InputFile[row,:] = data_list[row]
    return data_list, InputFlag
