param($installPath, $toolsPath, $package, $project)

# Prompt user to add project
#[System.Windows.MessageBox]::Show("Don`'t forget to add ../packages/OBSEPluginDevPackage/lib/common/common.vcxproj as a project to your solution." )

function someFunction {
   $a = "hello"
   "Function is running"
   return $a
}

#$b = someFunction
#$b = $b[($b.count - 1)]
#Write-host "$b"
$b = someFunction[-1]
$b = $b[($b.count - 1)]
Write-host "$b"




#function FindSln()
#{
#	$cSlnDirFiles = get-childitem (get-item $PSScriptRoot).parent.parent.parent.fullname
#	$cSlnFiles = $cSlnDirFiles | where {$_.extension -eq ".sln"}
#	Write-host "*********** ***********"
#	$cSlnFiles.GetType().Name
#	#$cSlnFiles | format-table name
#	#Write-host "*********** *********** ***********"
#	# If there are multiple .sln files, abort
#	return "hi"
#}
#
#
#
#
##  Find .sln
#$vSln = FindSln()

#  Retrieve project data from .proj

#  insert project data into .sln
