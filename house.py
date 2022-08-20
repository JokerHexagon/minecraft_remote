"""
Draw x, y, z axis in the Minecraft world
    x: stone
    y: grass/dirt
    z: gold
Flatten the world
    width: Size of flat world to produce.
           x, z: from -widh to width
           y: from AXIS_BOTTOM to AXIS_TOP

mc: an instance of Minecraft must be created beforehand
"""
# Select modules to import here.
# Minecraft Java Edition 1.16.5 : mcje, param_MCJE
# Minecraft Java Edition 1.12.2 : mcpi, param_MCJE1122
# Minecraft Pi Edition : mcpi, param_MCPI

from re import X
from mcje.minecraft import Minecraft
import param_MCJE1122 as param

# from mcpi.minecraft import Minecraft
# import param_MCJE1122 as param

# from mcpi.minecraft import Minecraft
# import param_MCPI as param


from time import sleep
import random

i = 1
color = 0

materials = (
    
    (
        (param.WOODEN_SLAB, 0),  #屋根
        (param.SANDSTONE, 2),    #壁
        (param.STONE, 6),        #土台
        (param.PLANKS, 2),       #床
        (param.SPRUCE_DOOR),     #ドア
    ),
    (
        (param.WOODEN_SLAB, 5),   #屋根
        (param.END_BRICKS, 0),   #壁
        (param.STONEBRICK, 0),   #土台
        (param.PLANKS, 1),       #床
        (param.OAK_DOOR),        #ドア
    ),
    (
        (param.STONE_SLAB, 6),   #屋根
        (param.QUARTZ_BLOCK, 0), #壁
        (param.COBBLESTONE, 0),  #土台
        (param.PLANKS, 0),       #床
        (param.DARK_OAK_DOOR),   #ドア
    ),
    (
        (param.STONE_SLAB, 4),   #屋根
        (param.TERRACOTTA, 0),   #壁
        (param.SANDSTONE, 0),    #土台
        (param.PLANKS, 3),       #床
        (param.DARK_OAK_DOOR),   #ドア
    ),
    (
        (param.STONE_SLAB, 0),   #屋根
        (param.CONCRETE),        #壁
        (param.STONE, 0),        #土台
        (param.PLANKS, 0),       #床
        (param.DARK_OAK_DOOR),   #ドア
    ),
)



def house(mc,x,z,color,angle,type):
    #　angleは1 or -1
    preset = 0
    if type >= 4:
        preset = 4
    else:
        preset = type
    if preset != 4:
        color = ()

    mc.setBlocks(x + 0 * angle, param.Y_SEA + 1, z + 0 * angle,   x + 7 * angle,param.Y_SEA + 1, z + 7 * angle, materials[preset][2])
    mc.setBlocks(x + 4 * angle, param.Y_SEA + 1, z + 5 * angle,   x + 11 * angle,param.Y_SEA + 1, z + 12 * angle, materials[preset][2])
    mc.setBlocks(x + 1 * angle, param.Y_SEA + 1, z + 1 * angle,   x + 6 * angle,param.Y_SEA + 1, z + 6 * angle, materials[preset][3])
    mc.setBlocks(x + 5 * angle, param.Y_SEA + 1, z + 6 * angle,   x + 10 * angle,param.Y_SEA + 1, z + 11 * angle, materials[preset][3])
    mc.setBlocks(x + 0 * angle, param.Y_SEA + 2, z + 0 * angle,   x + 7 * angle, param.Y_SEA + 6, z + 7 * angle,   materials[preset][1], color)
    mc.setBlocks(x + 0 * angle, param.Y_SEA + 7, z + 0 * angle,   x + 7 * angle, param.Y_SEA + 7, z + 7 * angle,   materials[preset][0])
    mc.setBlocks(x + 4 * angle, param.Y_SEA + 2, z + 5 * angle,   x + 11 * angle, param.Y_SEA + 11, z + 12 * angle,   materials[preset][1], color)
    mc.setBlocks(x + 4 * angle, param.Y_SEA + 12, z + 5 * angle,   x + 11 * angle, param.Y_SEA + 12, z + 12 * angle,   materials[preset][0])
    mc.setBlocks(x + 1 * angle, param.Y_SEA + 2, z + 1 * angle,   x + 6 * angle, param.Y_SEA + 5, z + 6 * angle,   param.AIR)
    mc.setBlocks(x + 5 * angle, param.Y_SEA + 2, z + 6 * angle,   x + 10 * angle, param.Y_SEA + 10, z + 11 * angle,   param.AIR)
    
    mc.setBlock(x + 0 * angle, 64, z + 1 * angle,     materials[preset][4], -angle + 1)
    mc.setBlock(x + 0 * angle, 65, z + 1 * angle,     materials[preset][4], -angle + 9)
    mc.setBlocks(x + 0 * angle, 64, z + 4 * angle,  x + 0 * angle, 66, z + 5 * angle,   param.STAIND_GLASS_PANE, 0)
    mc.setBlocks(x + 4 * angle, 66, z + 10 * angle,  x + 4 * angle, 67, z + 11 * angle,   param.STAIND_GLASS_PANE, 0)
    mc.setBlocks(x + 4 * angle, 71, z + 7 * angle,  x + 4 * angle, 72, z + 7 * angle,   param.STAIND_GLASS_PANE, 0)
    mc.setBlocks(x + 4 * angle, 71, z + 9 * angle,  x + 4 * angle, 72, z + 11 * angle,   param.STAIND_GLASS_PANE, 0)


def make_rode(mc, street):
    mc.setBlocks(-39, param.Y_SEA, street*-18+16,  -35, param.Y_SEA, street*19-17,  param.STONE)
    mc.setBlocks(-2, param.Y_SEA, street*-18+16,  2, param.Y_SEA, street*19-17,  param.STONE)
    mc.setBlocks(35, param.Y_SEA, street*-18+16,  39, param.Y_SEA, street*19-17,  param.STONE)
    #"""
    
    global z
    global i
    global x
    z = street*-18+16
    while i <= street:
        mc.setBlocks(-39, param.Y_SEA, z,  39, param.Y_SEA, z+4,  param.STONE)
        i += 1
        z += 37
    #"""

def reset_minecraft_world(mc, width=80):
    mc.setBlocks(-width, param.Y_SEA + 1, -width,   width, param.AXIS_TOP,    width,    param.AIR)
    mc.setBlocks(-width, param.Y_SEA,     -width,   width, param.Y_SEA,       width,    param.GRASS_BLOCK)

def set_houses(mc,ax,az):
    house(mc,ax + 0,az + 0,random.randrange(0,15,1),1,random.randrange(0,18,1))
    house(mc,ax + 0,az + 15,random.randrange(0,15,1),1,random.randrange(0,18,1))
    house(mc,ax + 25,az + 27,random.randrange(0,15,1),-1,random.randrange(0,18,1))
    house(mc,ax + 25,az + 12,random.randrange(0,15,1),-1,random.randrange(0,18,1))

if __name__ == "__main__":
    # his computer
    # mc = Minecraft.create(address='nao2g005.local', port=param.PORT_MC)
    # your computer
    mc = Minecraft.create(port=param.PORT_MC)

    mc.postToChat("axis_flat module main part")

    # if MCJE 1.12.2 or earlier
    # mc.player.setPos(0,100,0)
    # mc.setBlocks(-80, 60, -80,   80, 120, 80,   0)

    reset_minecraft_world(mc, width=130)
    # draw_XYZ_axis(mc, wait=0.2)
    # clear_XYZ_axis(mc, wait=0)
    make_rode(mc,2)
    # ドアが邪魔になったら
    # /kill @e[type=item]