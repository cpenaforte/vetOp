from UniOp import UniOp
from DuoOp import DuoOp

def main(numberVec,function,u,v='',axle='',angle=0):
    u=list(u)
    v=list(v)
    if numberVec == 1:
        for i in range(0,4):
             u.pop(i)
        u = [float(el) for el in u]
        uniOp = UniOp(u)
        if function == 'rotation':
            return 'New vector: '+str(uniOp.vecRot(angle,axle))
    elif numberVec == 2:
        for i in range(0,4):
            u.pop(i)
            v.pop(i)
        u = [float(el) for el in u]
        v = [float(el) for el in v]
        duoOp = DuoOp(u,v)
        if function == 'add':
            return 'New vector: '+str(duoOp.sumVet(u,v))
        elif function == 'sub':
            return 'New vector: '+str(duoOp.difVet(u,v))
        elif function == 'sca':
            return 'Scalar product: '+str(duoOp.scalarProd(u,v))
        elif function == 'vec':
            return 'New vector: '+str(duoOp.vecProd(u,v))
        else:
            return "Unindentified operation!"
