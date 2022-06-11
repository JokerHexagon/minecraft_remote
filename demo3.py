from mcje.minecraft import Minecraft
import param_MCJE as param

import axis_flat

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("demo3")

axis_flat.reset_minecraft_world(mc, width=45)
axis_flat.draw_XYZ_axis(mc, wait=0.1)