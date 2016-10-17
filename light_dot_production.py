import maya.cmds as cmds
def ld_node(*args):
    
    #p_shd = cmds.ls(sl=1)
    ##print p_shd[0]
    #sName = p_shd[0]
    
    if not(cmds.objExists("toon_samplerInfo")):
        si = cmds.shadingNode("samplerInfo", asUtility = True, n = "toon_samplerInfo")
    if not(cmds.objExists("toon_lightInfo")):
        li = cmds.shadingNode("lightInfo", asUtility = True, n = "toon_lightInfo")
        
    pm = cmds.shadingNode("plusMinusAverage", asUtility = True)
    vm = cmds.shadingNode("vectorProduct", asUtility = True)
    dot = cmds.shadingNode("vectorProduct", asUtility = True)
    rv = cmds.shadingNode("remapValue", asUtility = True)


    cmds.setAttr(pm+".operation", 2)
    cmds.setAttr(vm+".operation", 3)
    cmds.setAttr(vm+".normalizeOutput", 1)

    cmds.setAttr(dot+".operation", 1)
    cmds.setAttr(vm+".normalizeOutput", 1)
    cmds.setAttr(dot+".normalizeOutput", 1)

    cmds.setAttr(rv+".inputMin", -1)

    cmds.connectAttr(si+".normalCamera", vm+".input1")
    cmds.connectAttr(li+".lightPosition", pm+".input3D[0]")
    cmds.connectAttr(si+".pointWorld", pm+".input3D[1]")

    cmds.connectAttr(vm+".output", dot+".input1")
    cmds.connectAttr(pm+".output3D", dot+".input2")
    cmds.connectAttr(dot+".outputX", rv+".inputValue")
    
    cmds.shadingNode("useBackground", asShader = True )
    



ld_node()    





