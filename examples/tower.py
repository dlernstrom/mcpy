# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mcpi.block as block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x, y, z = position.x, position.y, position.z

mc.player.setTilePos(x, y, z)

for b in range(0, 10):
    mc.setBlock(x, y+b, z, 103)