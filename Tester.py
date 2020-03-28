from direct.actor.Actor import Actor
from panda3d.core import *
from direct.task import Task
import math
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import Point3
from pandac.PandaModules import *

import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import Vec3, Vec4, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
base.setBackgroundColor(0,150,255)
# TTC

ttc = loader.loadModel("phase_15/hood/toontown_central.bam")
ttc.reparentTo(render)
# pumpkin decor
shortPumpkin = loader.loadModel("phase_4/models/estate/pumpkin_short.bam")
shortPumpkin.reparentTo(render)
shortPumpkinTex = loader.loadTexture("phase_4/maps/pumpkin_short.jpg")
shortPumpkin.setTexture(shortPumpkinTex, 1)
shortPumpkin.setX(9.9)
shortPumpkin.setY(2.9)
shortPumpkin.setZ(3.9)
shortPumpkin.setHpr(270,0,0)
shortPumpkin.place()
#large BOi
tallPumpkin = loader.loadModel("phase_4/models/estate/pumpkin_tall.bam")
tallPumpkin.reparentTo(render)
tallPumpkinTex = loader.loadTexture("phase_4/maps/pumpkin_tall.jpg")
tallPumpkin.setTexture(tallPumpkinTex, 1)
tallPumpkin.setX(9.9)
tallPumpkin.setY(-3)
tallPumpkin.setZ(3.9)
tallPumpkin.setHpr(270,0,0)
tallPumpkin.place()






# Loanshark

LoanShark = Actor('phase_3.5/models/char/suitB-mod.bam', {'victory': 'phase_4/models/char/suitB-victory.bam'})
LoanShark.reparentTo(render)
LoanShark.loop('victory')
LoanSharkHead = loader.loadModel('phase_4/models/char/suitB-heads.bam').find('**/loanshark')
LoanSharkHead.reparentTo(LoanShark.find('**/joint_head'))
LoanSharkTorsoTex = loader.loadTexture('phase_3.5/maps/m_blazer.jpg')
LoanShark.find('**/torso').setTexture(LoanSharkTorsoTex, 1)
LoanSharkArmTex = loader.loadTexture('phase_3.5/maps/m_sleeve.jpg')
LoanShark.find('**/arms').setTexture(LoanSharkArmTex, 1)
LoanSharkLegTex = loader.loadTexture('phase_3.5/maps/m_leg.jpg')
LoanShark.find('**/legs').setTexture(LoanSharkLegTex, 1)

# Loanshark pos
LoanShark.setX(10)
LoanShark.setZ(4)
LoanShark.setH(90)

LoanShark.place()




#toonBoi


base.oobe()
run()