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

from mcje.minecraft import Minecraft
import param_MCJE1122 as param

# from mcpi.minecraft import Minecraft
# import param_MCJE1122 as param

# from mcpi.minecraft import Minecraft
# import param_MCPI as param


from time import sleep





def house(mc,x,z,color):
    
    
    mc.setBlocks(x + 0, param.Y_SEA + 1, z + 0,   x + 7,param.Y_SEA + 1, z + 7, param.STONE)
    mc.setBlocks(x + 4, param.Y_SEA + 1, z + 5,   x + 11,param.Y_SEA + 1, z + 12, param.STONE)
    mc.setBlocks(x + 1, param.Y_SEA + 1, z + 1,   x + 6,param.Y_SEA + 1, z + 6, param.OAK_PLANKS)
    mc.setBlocks(x + 5, param.Y_SEA + 1, z + 6,   x + 10,param.Y_SEA + 1, z + 11, param.OAK_PLANKS)
    mc.setBlocks(x + 0, param.Y_SEA + 2, z + 0,   x + 7, param.Y_SEA + 6, z + 7,   param.CONCRETE, color)
    mc.setBlocks(x + 0, param.Y_SEA + 7, z + 0,   x + 7, param.Y_SEA + 7, z + 7,   param.STONE_SLAB)
    mc.setBlocks(x + 4, param.Y_SEA + 2, z + 5,   x + 11, param.Y_SEA + 11, z + 12,   param.CONCRETE, color)
    mc.setBlocks(x + 4, param.Y_SEA + 12, z + 5,   x + 11, param.Y_SEA + 12, z + 12,   param.STONE_SLAB)
    mc.setBlocks(x + 1, param.Y_SEA + 2, z + 1,   x + 6, param.Y_SEA + 5, z + 6,   param.AIR)
    mc.setBlocks(x + 5, param.Y_SEA + 2, z + 6,   x + 10, param.Y_SEA + 10, z + 11,   param.AIR)
    
    mc.setBlock(x + 0, 64, z + 1,     param.DARK_OAK_DOOR, 0)
    mc.setBlock(x + 0, 65, z + 1,     param.DARK_OAK_DOOR, 8)
    mc.setBlocks(x + 0, 64, z + 4,  x + 0, 66, z + 5,   param.STAIND_GLASS_PANE, 0)
    mc.setBlocks(x + 4, 66, z + 10,  x + 4, 67, z + 11,   param.STAIND_GLASS_PANE, 0)
    mc.setBlocks(x + 4, 71, z + 7,  x + 4, 72, z + 7,   param.STAIND_GLASS_PANE, 0)
    mc.setBlocks(x + 4, 71, z + 9,  x + 4, 72, z + 11,   param.STAIND_GLASS_PANE, 0)


def reset_minecraft_world(mc, width=80):
    mc.setBlocks(-width, param.Y_SEA + 1, -width,   width, param.AXIS_TOP,    width,    param.AIR)
    mc.setBlocks(-width, param.Y_SEA,     -width,   width, param.Y_SEA,       width,    param.GRASS_BLOCK)


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
    house(mc,0,0,16)