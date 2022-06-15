import numpy as np

class UniOp(object):

    def __init__(self,u):
        self.u = np.array(u)

    def vecRot(self,radAngle,axle):
        c = np.cos(float(radAngle))
        s = np.sin(float(radAngle))

        if axle == 'z':
            self.rotMatrix = np.matrix([(c,-s,0),(s,c,0),(0,0,1)])
        elif axle == 'y':
            self.rotMatrix = np.matrix([(c,0,-s),(0,1,0),(s,0,c)])
        elif axle == 'x':
            self.rotMatrix = np.matrix([(1,0,0),(0,c,-s),(0,s,c)])
        else:
            print("Unindentified axle, type 'x', 'y' or 'z'")

        self.newU = np.matmul(self.rotMatrix,self.u)
        self.newU = self.newU.tolist()[0]
        self.newU = [round(num,3) for num in self.newU]
        return self.newU