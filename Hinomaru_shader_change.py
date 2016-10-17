import maya.cmds as cmds
hi_sels = cmds.ls(typ="HinomaruShader")

for x in hi_sels:

    cs = x+".ColorSampler"
    os = x+".outColor"
    bs = cmds.getAttr(x+".BaseColor")
    bl = cmds.connectionInfo(cs, id=True)

    outl = cmds.connectionInfo(os, isSource=True)
    outc = cmds.connectionInfo(os, dfs=True)
    
    if outl:
        
        vs = cmds.shadingNode("MaroToonShader", asShader=True, n = x)
        
        x = outc[0].split(".")
        x = x[0]
        cmds.disconnectAttr(os, outc[0])
        cmds.connectAttr(vs+".outColor", outc[0])
        
        if bl :
            
            # Connect Hinomaru ColorSampler File Texture to layeredTexture
            c_name = cmds.connectionInfo(cs, sfd=True)
            cmds.connectAttr(c_name, vs+".color")
            #cmds.connectAttr(lt+".outColor",  vs+".outColor")
                    
            
        else : 
            cmds.setAttr(vs+".color",bs[0][0],bs[0][1],bs[0][2])
            #cmds.connectAttr(lt+".outColor",  vs+".outColor")
            
