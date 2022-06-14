import numpy as np

class DuoOp(object):

  def __init__(self,u,v):
    self.u = np.array(u)
    self.v = np.array(v)

  def sumVet(self,u,v):
    return np.add(u,v).tolist()

  def difVet(self,u,v):
    return np.subtract(u,v).tolist()

  def scalarProd(self,u,v):
    return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]

  def vecProd(self,u,v):
    vet = []

    vet.append(u[1]*v[2]-u[2]*v[1])
    vet.append(u[2]*v[0]-u[0]*v[2])
    vet.append(u[0]*v[1]-u[1]*v[0])

    return vet