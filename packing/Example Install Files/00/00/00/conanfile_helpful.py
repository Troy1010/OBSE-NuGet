from conans import ConanFile
import subprocess
import xml.etree.ElementTree
import os

class TM_HelloWorld_Conan(ConanFile):
    name="HelloWorld"
    requires="OBSEPluginDevPackage/0.1@Troy1010/channel","vistualstudio_PTL/0.1@Troy1010/channel"
    generators = "visual_studio"

    sMainProjFolder = 'HelloWorld'

    def imports(self):
        #---Import files
        self.copy('*',src='deploy',dst=self.sMainProjFolder)
        #---HookBuildInfo
        #!Assume user already installed HookBuildInfo
        import BuildInfoIntegration as BII
        if "visual_studio" in self.generators:
            BII.HookBuildInfo('HelloWorld/HelloWorld.vcxproj','conanbuildinfo.props')
        import VisualStudioAutomation as VSA
        import TM_CommonPy as TMC
        vDTE = VSA.InstantiateDTE()
        vProj = VSA.OpenProj(vDTE,'HelloWorld/HelloWorld.vcxproj')
        vTree = xml.etree.ElementTree.parse('conanbuildinfo.props')
        vElemToFind = xml.etree.ElementTree.Element("Conan-OBSEPluginDevPackage-Root")
        sOBSEPluginDevRoot = TMC.FindElem(vElemToFind,vTree).text
        sRoot = os.path.join(sOBSEPluginDevRoot,"include","obse","obse")
        cOBSEFiles = [os.path.join("..","StdAfx.cpp"),os.path.join("..","StdAfx.h"),
        "GameActorValues.cpp","GameActorValues.h","GameAPI.cpp","GameAPI.h",
        "GameBSExtraData.cpp","GameBSExtraData.h","GameData.cpp","GameData.h",
        "GameExtraData.cpp","GameExtraData.h","GameForms.cpp","GameForms.h",
        "GameObjects.cpp","GameObjects.h","GameRTTI_1_1.inl","GameRTTI_1_2.inl",
        "GameRTTI_1_2_416.inl","GameTasks.cpp","GameTasks.h","GameTypes.cpp","GameTypes.h",
        "NiAPI.cpp","NiAPI.h","NiNodes.cpp","NiNodes.h","NiRTTI.cpp","NiRTTI.h",
        "ParamInfos.h","PluginAPI.h","Script.cpp","Script.h","Utilities.cpp","Utilities.h"]
        for vItem in cOBSEFiles:
            VSA.AddFileToProj(vProj,os.path.join(sRoot,vItem),"obse")
        vProj.Save()
#        VSA.AddFileToProj(vProj,os.path.join(sOBSEPluginDevRoot,"include","obse","StdAfx.h"),"obse")
        VSA.QuitDTE(vDTE)
