#Programa de Carlos Penaforte
#Esse programa realiza a rotacao de um conjunto de pontos em relacao a um eixo cartesiano
import numpy as np
class Rotacao(object):
    def __init__(self,x,y,z,eixo):
        self.Vx = x
        self.Vy = y
        self.Vz = z
        self.eixo = str(eixo)
    def rot_ponto(self,ang_rad):
        #Realiza rotacao em torno do eixo dado no sentido anti-horario
        self.Ponto = np.array([self.Vx,self.Vy,self.Vz])
        c = np.cos(ang_rad)
        s = np.sin(ang_rad)
        if self.eixo == 'z':
            self.Matriz_rot = np.matrix([(c,-s,0),(s,c,0),(0,0,1)])
        elif self.eixo == 'y':
            self.Matriz_rot = np.matrix([(c,0,-s),(0,1,0),(s,0,c)])
        elif self.eixo == 'x':
            self.Matriz_rot = np.matrix([(1,0,0),(0,c,-s),(0,s,c)])
        else:
            print "eixo mal especificado, digite 'x', 'y' ou 'z'"
        self.NovoPonto = np.matmul(self.Matriz_rot,self.Ponto)
        return self.NovoPonto

    
