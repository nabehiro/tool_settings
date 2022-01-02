# enable posh-git prompt on oh-my-posh.
# https://ohmyposh.dev/docs/poshgit
$env:POSH_GIT_ENABLED = $true

Import-Module posh-git
Import-Module oh-my-posh

# use oirignal oh my posh config.
Set-PoshPrompt -Theme ~/omp.json

# install prerelease(2.2.0-beta4) PSReadLine
# Install-Module -Name PSReadLine -AllowPrerelease -Force
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows
