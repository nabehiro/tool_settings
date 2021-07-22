# enable posh-git prompt on oh-my-posh.
# https://ohmyposh.dev/docs/poshgit
$env:POSH_GIT_ENABLED = $true

Import-Module posh-git
Import-Module oh-my-posh

# use oirignal oh my posh config.
Set-PoshPrompt -Theme ~/omp.json

Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows