from time import sleep
from house import house, make_rode, reset_minecraft_world, set_houses
from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import random



mc = Minecraft.create(port=param.PORT_MC)
#"""
#  白い家を出す
reset_minecraft_world(mc, width=130)
house(mc,0,0,0,1,4)
sleep(15)
# 16色の家を並べる
reset_minecraft_world(mc, width=130)
sleep(3)
ax, az,color = 0, -60, 0
while ax <= 30:
    while az <= 45:
        house(mc,ax,az,color,1,4)
        az += 15
        color +=1
        sleep(1)
    ax += 30
    az = -60
sleep(7)    
#コンクリートの家以外をつくる
reset_minecraft_world(mc,width=130)
sleep(3)
type, az =0, -30
while az < 30:
    house(mc,0,az,0,1,type)
    az += 15
    type +=1
    sleep(1)
sleep(7)
#"""    

#街をつくる
reset_minecraft_world(mc, width=130)
sleep(3)
streetline = 2
az = streetline * -35 + 21
j = 1
make_rode(mc, streetline * 2)
sleep(2)
while j <= streetline * 2 - 1:
    set_houses(mc,-31,az)
    set_houses(mc,6,az)
    az += 37
    j += 1
