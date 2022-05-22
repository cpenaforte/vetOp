from Modulos import Operations as op
def main():
    encerrar = 'nao'
    while encerrar == 'nao':
        #recursividade que depende do usuario
        x = input("Digite o valor do ponto no eixo x: ")
        y = input("Digite o valor do ponto no eixo y: ")
        z = input("Digite o valor do ponto no eixo z: ")
        eixo = str(input("Digite o eixo de rotacao: "))
        rot = op.Rotacao(x,y,z,eixo)
        ang = input("Digite o angulo de rotacao em radianos: ")
        print 'Novo ponto: '+str(rot.rot_ponto(ang))
        encerrar = input("Deseja encerrar programa? Digite 'sim' ou 'nao': ")
if __name__=="__main__":
    main()
    
