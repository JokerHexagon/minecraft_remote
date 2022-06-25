from demo4 import house, reset_minecraft_world
from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import random

random.randrange(0,15,1)

mc = Minecraft.create(port=param.PORT_MC)

reset_minecraft_world(mc, width=130)
ax, az,color = 0, -60, 0
while ax <= 30:
    while az <= 45:
        house(mc,ax,az,color)
        az += 15
        color +=1
    ax += 30
    az = -60