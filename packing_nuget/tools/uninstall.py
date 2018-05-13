# rough draft
#todo: maybe make it so .py can run on its own without pyton installed.


import os, sys, glob
import xml.etree.ElementTree
from pathlib import Path

sThisScriptName = os.path.basename(sys.argv[0])
print(sThisScriptName+"\Open")

def GetScriptRoot():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def AddProjToSln_Undo(sUninstallInfoFile, sSlnFile):
    #  Open
    print("AddProjToSln_Undo\\Open")
    print("sSlnFile:\t\t\t"+sSlnFile)
    print("sUninstallInfoFile:\t"+sUninstallInfoFile)
    #  Retrieve sToRemoveFromSln from UninstallInfo.txt
    vUninstallInfo = open(sUninstallInfoFile,'r')
    sToRemoveFromSln = vUninstallInfo.read()
    vUninstallInfo.close()
    #  Remove sToRemoveFromSln from sSlnFile
    vSlnFile = open(sSlnFile,"r+")
    vCopyOfSlnFile = vSlnFile.read()
    vSlnFile.seek(0)
    vSlnFile.write(vCopyOfSlnFile.replace(sToRemoveFromSln,""))
    vSlnFile.truncate()
    vSlnFile.close()
    #  Close
    print("AddProjToSln_Undo\\Close")


#  Find sUninstallInfoFile
sUninstallInfoFile = GetScriptRoot() + "\\UninstallInfo.txt"
if not os.path.isfile(sUninstallInfoFile):
    print(sThisScriptName+"\ERROR\Could not locate UninstallInfo.txt at "+sUninstallInfoFile+". You'll have to remove the library's project from your solution on your own.")
    quit()

# Remove library's project from consumer's sln
#assume sSlnFile was passed to this script as 1st argument
AddProjToSln_Undo(sUninstallInfoFile, sys.argv[1])


















#  close
print(sThisScriptName+"\Close")
