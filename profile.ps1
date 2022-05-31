# https://ohmyposh.dev/docs/installation/windows
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\wopian.omp.json" | Invoke-Expression

# https://github.com/devblackops/Terminal-Icons
Import-Module -Name Terminal-Icons

# https://github.com/PowerShell/PSReadLine
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows
