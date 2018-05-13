param($installPath, $toolsPath, $package, $project)

#-I should check if the consumer has python
python $PSScriptRoot\install.py $dte.Solution.FullName
