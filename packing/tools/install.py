# rough draft
#todo: make uninstall.py, maybe make it so .py can run on its own without pyton installed.

import os, sys, glob
import xml.etree.ElementTree
from pathlib import Path

sThisScriptName = os.path.basename(sys.argv[0])
print(sThisScriptName+"\Open")

def GetScriptRoot():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def AddProjToSln(sProjFile, sSlnFile):
    #  Open & Parse sProjFile
    print("sSlnFile:\t"+sSlnFile)
    print("sProjFile:\t"+sProjFile)
    vTree = xml.etree.ElementTree.parse(sProjFile)
    vRoot = vTree.getroot()
    #  Retrieve ProjectGUID from sProjFile
    for vFound in vTree.iter():
        if "ProjectGuid" in vFound.tag:
            sProjectGuid = vFound.text
            break
    if not sProjectGuid:
        print("AddProjToSln\ERROR\Could not extract ProjectGuid. You'll have to add the library's project to your solution on your own.")
        quit()
    #  Retrieve ProjectTypeGUID from sProjFile
    #-There can be multiple sConfigurationType for different targets. How to handle that?
    for vFound in vTree.iter():
        if "ConfigurationType" in vFound.tag:
            sConfigurationType = vFound.text
            break
    if not sConfigurationType:
        print("AddProjToSln\ERROR\Could not extract sConfigurationType. You'll have to add the library's project to your solution on your own.")
        quit()
    # ProjectTypeGUIDs are not written in the sProjFile file. Instead, they contain sConfigurationType which has a ProjectTypeGUID enum
    if sConfigurationType == "StaticLibrary":
        sProjectTypeGUID = "{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}"
    else:
        print("AddProjToSln\ERROR\Could not match sConfigurationType to a sProjectTypeGUID. You'll have to add the library's project to your solution on your own.")
        quit()
    #  Determine sProjName
    sProjName = os.path.splitext(os.path.basename(sProjFile))[0]
    #  Determine sProjFileRelativeToSln
    sProjFileRelativeToSln = os.path.relpath(sProjFile, os.path.dirname(sSlnFile))
    #  Determine sToWriteIntoSln
    sToWriteIntoSln = "\nProject(\""+sProjectTypeGUID+"\") = \""+sProjName+"\", \""+sProjFileRelativeToSln+"\", \""+sProjectGuid+"\"\nEndProject"
    #  Save sToWriteIntoSln so it can be read on uninstall
    vUninstallInfo = open(GetScriptRoot()+'\\UninstallInfo.txt','w')
    vUninstallInfo.write(sToWriteIntoSln)
    vUninstallInfo.close()
    #  Write into Sln
    vSlnFile = open(sSlnFile,"a+")
    vSlnFile.write(sToWriteIntoSln)
    vSlnFile.close()



#  Find sLibProjFile
sLibProjFile = str(Path(GetScriptRoot()).parent) + "\\lib\\common\\common.vcxproj"
if not os.path.isfile(sLibProjFile):
    print(sThisScriptName+"\ERROR\Could not locate the library's project file at "+sLibProjFile+". You'll have to add the library's project to your solution on your own.")
    quit()

# Add library's project to consumer's sln
#assume sSlnFile was passed as 1st argument to this script
AddProjToSln(sLibProjFile, sys.argv[1])


















#  close
print(sThisScriptName+"\Close")
