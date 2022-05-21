#Programa de Carlos Penaforte
#Esse programa realiza a rotacao de um conjunto de pontos em relacao a um eixo cartesiano
import numpy as np
class Rotacao(object):
    def __init__(x,y,z,eixo,self):
        self.Px = x
        self.Py = y
        self.Pz = z
        self.eixo = str(eixo)
    def rot_ponto(ang_rad):
        self.Ponto = np.array([self.Px,self.Py,self.Pz])
        c = np.cos(ang_rad)
        s = np.sen(ang_rad)
        if self.eixo == 'x':
            Matriz_rot = np.array([[c,-s,0],[s,c,0],[0,0,1]])
        elif self.eixo == 'y':
            Matriz_rot = np.array([[c,0,-s],[0,1,0],[s,0,c]])
        elif self.eixo == 'z':
            Matriz_rot = np.array([[1,0,0],[0,c,-s],[0,s,c]])
        else:
            print "eixo mal especificado, digite 'x', 'y' ou 'z'"
        self.NovoPonto = self.Ponto*Matriz_rot
        return self.NovoPonto
def main():
    encerrar = 'nao'
    while encerrar == 'nao':
        x = float(input("Digite o valor do ponto no eixo x: "))
        y = float(input("Digite o valor do ponto no eixo y: "))
        z = float(input("Digite o valor do ponto no eixo z: "))
        eixo = str(input("Digite o eixo de rotacao: "))
        rot = Rotacao(x,y,z,eixo)
        ang = input("Digite o angulo de rotacao em radianos: ")
        print rot_ponto(ang)
        encerrar = input("Deseja encerrar programa? Digite 'sim' ou 'nao': ")
if __name__=="__main__":
    main()
    
