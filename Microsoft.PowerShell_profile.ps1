
################################################################################
# Reference to posh-git.example 'C:\tools\posh-git\profile.example.ps1'
################################################################################

# Load posh-git module 
Import-Module posh-git

# If module is installed in a default location ($env:PSModulePath),
# use this instead (see about_Modules for more information):
# Import-Module posh-git


# Set up a simple prompt, adding the git prompt parts inside git repos
function global:prompt {
    Write-Host "@ " -NoNewLine -ForegroundColor darkred
    Write-Host $pwd.ProviderPath.Replace($HOME, "~") -nonewline -foregroundcolor blue
    Write-VcsStatus
    Write-Host ""
    Write-Host ">" -NoNewLine -foregroundcolor blue
    return " "
}

Start-SshAgent -Quiet
