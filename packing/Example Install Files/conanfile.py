from conans import ConanFile
import xml.etree.ElementTree
import os, sys, ctypes
import VisualStudioAutomation as VS
import TM_CommonPy as TM

if __name__ == "__main__":
    try:
        #---Open
        sProj = os.path.join("HelloWorld","HelloWorld.vcxproj")
        #---
        TM.Run("conan install . -pr conanprofile_OBSEPlugin")
        VS.SetTMDefaultSettings(sProj)
        VS.IntegrateProps(sProj,"conanbuildinfo.props")
        ##region Integrate OBSEPluginDevPackage RecommendedIntegrationFiles
        with TM.ElementTreeContext("conanbuildinfo.props") as vTree:
            sOBSEPluginDevPackageRoot = TM.FindElem(xml.etree.ElementTree.Element("Conan-OBSEPluginDevPackage-Root"),vTree).text
        sys.path.insert(0,sOBSEPluginDevPackageRoot)
        import RecommendedIntegration
        RecommendedIntegration.Main(os.path.abspath(sProj),sOBSEPluginDevPackageRoot)
        ##endregion
    except:
        ctypes.windll.user32.MessageBoxW(0, "Exception occured.", "conanfile.py", 1)
        raise

class TM_HelloWorld_Conan(ConanFile):
    name="HelloWorld"
    requires="OBSEPluginDevPackage/0.1@Troy1010/channel"
    generators = "visual_studio"
