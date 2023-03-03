from visual import*

scene = display(width = 500, height = 500, range = 10**11*5)

sun = sphere(pos=(0,0,0),radius=10**10*3,color=color.yellow)
terra = sphere(pos=vector(150*10**9,0,0),radius=10**10,color=color.blue,
               make_trail=True)
terra.v=vector(0,30e3,0)

Ms = 2*10**30
G = 6.67*10**-11

t = 0
dt = 36000
while True:
    rate(1000)
    
    QTerra=(-G*Ms)/mag(terra.pos)**3*terra.pos

    terraVold = terra.v
    terra.v = terraVold + QTerra*dt

    terraPosOld = terra.pos
    terra.pos = terraPosOld + terra.v*dt
    
    print(terra.pos)
    t+=dt
