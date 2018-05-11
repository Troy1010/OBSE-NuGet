param($installPath, $toolsPath, $package, $project)

Write-Host "install.ps1\Open"

$sProjFile = Resolve-Path -Path "$PSScriptRoot\..\lib\common\common.vcxproj"
Write-Host "sProjFile:$sProjFile"
#$dte.Solution.AddProjToSln($sProjFile)
#$dte.Solution.Properties.Item("StartupProject").Value #Works
#$dte.Solution.FullName
$dte.Solution.AddFromFile($sProjFile,$TRUE)

Write-Host "install.ps1\Close"
