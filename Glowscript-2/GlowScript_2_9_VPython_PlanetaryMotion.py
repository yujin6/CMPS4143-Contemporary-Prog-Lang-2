GlowScript 2.9 VPython

"""
@author: Yujin Yoshimura
CMPS 4553 Computational Methods
Dr. Tina Johnson
Program 4

This program simulates a Solar System with Kepler's laws of planetary motion.
The heavenly bodies simulated are Sun, Mercury, Venus, Earth, and Mars.
Each heavenly bodies have their own mass. Gravitational force between any two
heavenly bodies are calculated, which yields acceleration, velocity and
position of each of the heavenly bodies. Leap frog method is used to
demonstrate each iteration.
"""

scene.caption = """In GlowScript programs:
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
scene.forward = vector(0,-.3,-1)

# Determines the resultant force from star i to the other bodies.
# Since this calculates each force between to bodies twice its not particularly
# efficient, should use table but what the heck.
# Note that since the app does not resultant in bodies getting close to each
# other, we do not need to add code to prevent infinite forces from being
# created when using point masses.:>)
def Force(slist,i):
    # force vector
    force = vector(0,0,0)
    for j in range(3):
        if i != j:
            # dir is a vector from i to j
            dir = slist[j].pos-slist[i].pos
            # unit vector from i to j
            dir = norm(dir)
            Fmag = (k * slist[i].mass * slist[j].mass / Distsq(slist[i].pos,slist[j].pos))
            force += Fmag * dir
    #resultant force
    return force
    
def Distsq(s1,s2):
   d = pow(mag(s1 - s2), 2)
   return d


# gravitational constant
k = 0.01
# length of trail
t = 1
# animation speed
speed = 200

sun     = sphere (pos=vector(0,0,0),  radius = 1.0, color = vector(1.0,1.0,0.6),
                  make_trail=True, interval=2, retain=200 * t)
mercury = sphere (pos=vector(-4,0,0), radius = 0.1, color = vector(0.6,0.6,0.6),
                  make_trail=True, interval=2, retain=80 * t)
venus   = sphere (pos=vector(0,0,-7), radius = 0.2, color = vector(1.0,0.8,0.2),
                  make_trail=True, interval=2, retain=180 * t)
earth   = sphere (pos=vector(0,0,10), radius = 0.2, color = vector(0.0,0.2,1.0),
                  make_trail=True, interval=2, retain=310 * t)
mars    = sphere (pos=vector(15,0,0), radius = 0.1, color = vector(0.8,0.4,0.0),
                  make_trail=True, interval=2, retain=540 * t)

# set mass
sun.mass     = 1000
mercury.mass = 0.1
venus.mass   = 1.2
earth.mass   = 2.0
mars.mass    = 0.2

# set initial velocity
sun.p     = vector(0.0,0,0)
mercury.p = vector(0,0,1.6)
venus.p   = vector(-1.2,0,0)
earth.p   = vector(1.0,0,0)
mars.p    = vector(0,0,-0.8)

# set initial acceleration
sun.a     = vector(0,0,0)
mercury.a = vector(0,0,0)
venus.a   = vector(0,0,0)
earth.a   = vector(0,0,0)
mars.a    = vector(0,0,0)

a = [vector(0,0,0),vector(0,0,0)]
slist = [sun, mercury, venus, earth, mars]
dt=.1


while True:
    rate(speed)
    # calculate next position of every star
    for i in range(len(slist)):
        # get next position
        slist[i].pos += (dt*slist[i].p + .5*dt*dt*slist[i].a)
        # save this accel for leapfrog calculations
        a[i] = slist[i].a
        
    # now calculate the next accel and velocity
    for i in range(len(slist)):
        # uses pos and mass only
        F = Force(slist,i)
        # new accel from F = ma
        slist[i].a = F / slist[i].mass
        # new vel using leap frog integration
        slist[i].p += .5*dt*(slist[i].a + a[i])