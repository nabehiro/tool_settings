
# Load posh-git example profile
. 'C:\tools\posh-git\profile.example.ps1'

# change prompt color
function prompt
{
  Write-Host "@" -NoNewLine -ForegroundColor yellow
  Write-Host "$(Convert-Path $(get-location))>" -nonewline -foregroundcolor blue
  return ' '
}
