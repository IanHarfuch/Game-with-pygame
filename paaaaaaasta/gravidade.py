from visual import*
ec = 0
epg = 0
a = vector(0,0,0)
b = vector(0,0,0)
def teste(a,b):
    resultado = a.x*b.x+a.y*b.y+b.z*a.z
    return resultado
grav = vector(0,-10,0)
solo = box(pos = vector(0,0,0), size = vector(10,1,10), color = color.yellow)
bolinha = sphere(pos = vector(0,10,0), radius = 0.5, color = color.red)
t = 0 
m = 2
w = 0
dt = 0.0001
FRAME = 1/dt
bolinha.velocity = vector(0,0,0)
while True:
    rate(FRAME)
    bolinha.pos += bolinha.velocity * dt
    bolinha.acel = grav
    f = m * bolinha.acel
    bolinha.velocity += grav * dt
    resultado = teste(f,bolinha.velocity)
    w += resultado  * (bolinha.velocity.mag * dt)
    ec = (m * bolinha.velocity.mag*bolinha.velocity.mag)/2
    r = bolinha.pos - solo.pos
    epg = m * grav.mag * r.mag
    t+=dt
    print (w, ec, epg)
    if (bolinha.pos.y <= solo.pos.y - (bolinha.radius + solo.size.y/2.0)
       or bolinha.pos.y <= solo.pos.y + (bolinha.radius + solo.size.y/2.0)):
            bolinha.velocity.y *= -1
            print (bolinha.acel)
