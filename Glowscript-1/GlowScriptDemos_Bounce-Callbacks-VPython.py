GlowScript 2.9 VPython

"""
@author: Yujin Yoshimura
CMPS 4553 Computational Methods
Dr. Tina Johnson
Program 3

This program simulates a bouncing ball by a simple loop where you update the
position and velocity vectors each iteration. Also the reduction of the height
of the bounce is simulated, resulting from energy loss when contacting with the
box. In order to get the ball to actually stop, the friction with the surface
of the box is simulated.
"""

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3), color = color.red)
wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3), color = color.red)
wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3), color = color.blue)
wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3), color = color.blue)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

ball = sphere (color = color.green, radius = 0.4, make_trail=True, retain=200)
ball.mass = 1.0
ball.p = vector (-0.15, +0.73, +0.27)

side = side - thk*0.5 - ball.radius

dt = 0.1
while True:
    rate(200)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    if not (side > ball.pos.x > -side):
        ball.p.x = -ball.p.x
    if not (side > ball.pos.y > -side):
        ball.p.y = -ball.p.y * 0.9
    if not (side > ball.pos.z > -side):
        ball.p.z = -ball.p.z
    if (ball.pos.y > -side):
        ball.p.y = ball.p.y - 0.01
    else:
        ball.p.x = ball.p.x * 0.998
        ball.p.z = ball.p.z * 0.998