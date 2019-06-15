# https://github.com/dahlbyk/posh-git

# Load posh-git module 
Import-Module posh-git

$GitPromptSettings.DefaultPromptPath.ForegroundColor = 0x8A2BE2
$GitPromptSettings.DefaultPromptSuffix.ForegroundColor = 0xADD8E6

function prompt {
    # Your non-prompt logic here

    # Have posh-git display its default prompt
    & $GitPromptScriptBlock
}
