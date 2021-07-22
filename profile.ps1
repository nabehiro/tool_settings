Import-Module posh-git
Import-Module oh-my-posh

# use oirignal oh my posh config.
Set-PoshPrompt -Theme ~/omp.json

Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows