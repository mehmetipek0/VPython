from visual import *
import random

ball=sphere(pos=(0,0,0), radius=0.5, color=color.white)
velocityX = random.random()
velocityY = random.random()
velocityZ = random.random()
ball.vel=vector(velocityX,velocityY,velocityZ)
wallTop = box(pos=(0,5,0), size=(10,1,10),color=color.magenta)
wallGround = box(pos=(0,-5,0), size=(10,1,10),color=color.yellow)
wallRight = box(pos=(5,0,0), size=(1,10,10),color=color.cyan)
wallLeft = box(pos=(-5,0,0), size=(1,10,10),color=color.red)
wallBack = box(pos=(0,0,-5), size=(10,10,1),color=color.green)

scene = display(width=500,height=500)
for counter in arange(0,100,0.01):
    rate(1000)
    ball.pos = ball.pos + ball.vel*0.01
    if abs(ball.pos.x) >= wallRight.pos.x-1:
        ball.vel.x = -ball.vel.x
        if ball.vel.x<0:
            ball.color = wallRight.color
        else:
            ball.color = wallLeft.color
    if abs(ball.pos.y) >= wallTop.pos.y-1:
        ball.vel.y = -ball.vel.y
        if ball.vel.y < 0:
            ball.color = wallTop.color
        else:
            ball.color = wallGround.color
    if abs(ball.pos.z) >= -(wallBack.pos.z+1):
        ball.vel.z = -ball.vel.z
        if ball.vel.z < 0:
            ball.color = color.white
        else:
            ball.color = wallBack.color
