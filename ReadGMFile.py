


def ReadGMFile():
    with open (inFile, "r") as myfile:
        data = myfile.read().splitlines()
        sp = data[3].split(' ')
        NumPts = int(sp[2].split(',')[0])
        dt = float(sp[4])
        hdlines = 4 
        
        for k in range(0,hdlines):
            del data [0]
        
        thefile = open(outFile, 'w')
        for item in data:
            thefile.write("%s\n" % item)
        thefile.close()
        
        data = list(filter(str.strip, data)) 
        #gm = np.reshape(np.asarray([float(j) for j in data]), (-1,1))
        gm = np.array(list(map(float, data)))
        gmXY[i+1] = gm
        
        
        del data
        del gm
        
        return dt,NumPts,gmXY