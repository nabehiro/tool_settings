export PATH="$HOME/bin:$PATH"

#----------------------------------------------------------------------
# node.js
#----------------------------------------------------------------------
export NODE_PATH="/usr/local/lib/node_modules"

#----------------------------------------------------------------------
# general
#----------------------------------------------------------------------
# auto change directory
setopt auto_cd

# auto directory pushd that you can get dirs list by cd -[tab]
setopt auto_pushd

# command correct edition before each completion attempt
setopt correct

# compacked complete list display
setopt list_packed

# no remove postfix slash of command line
setopt noautoremoveslash

# no beep sound when complete list displayed
setopt nolistbeep

# emacs like keybind (e.x. Ctrl-a goes to head of a line and Ctrl-e goes to end of it)
bindkey -e

# load colors
autoload -U colors; colors

#----------------------------------------------------------------------
# historical backward/forward search with linehead string binded to ^P/^N
#----------------------------------------------------------------------
autoload history-search-end
zle -N history-beginning-search-backward-end history-search-end
zle -N history-beginning-search-forward-end history-search-end
bindkey "^p" history-beginning-search-backward-end
bindkey "^n" history-beginning-search-forward-end
bindkey "\\ep" history-beginning-search-backward-end
bindkey "\\en" history-beginning-search-forward-end

#----------------------------------------------------------------------
# Command history configuration
#----------------------------------------------------------------------
HISTFILE=~/.zsh_history
HISTSIZE=50000
SAVEHIST=50000
setopt hist_ignore_dups # ignore duplication command history list
setopt share_history # share command history data

#----------------------------------------------------------------------
# Completion configuration
#----------------------------------------------------------------------
fpath=(${HOME}/.zsh/functions/Completion ${fpath})
autoload -U compinit promptinit
compinit
zstyle ':completion::complete:*' use-cache true
#zstyle ':completion:*:default' menu select true
zstyle ':completion:*:default' menu select=1
# ignore case
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'
# use completion color
zstyle ':completion:*' list-colors "${LS_COLORS}"
# kill
# zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([%0-9]#)*=0=01;31'
# sudo
#zstyle ':completion:*:sudo:*' command-path /usr/local/sbin /usr/local/bin /usr/sbin /usr/bin /sbin /bin /usr/X11R6/bin

#----------------------------------------------------------------------
# Alias configuration
#----------------------------------------------------------------------
# expand aliases before completing
setopt complete_aliases # aliased ls needs if file/dir completions work

alias where="command -v"
alias j="jobs -l"
alias du="du -h"
alias df="df -h"
alias su="su -l"
# ls
alias ls="ls -G -w"
alias la="ls -a"
alias lf="ls -F"
alias ll="ls -l"
alias lla="ls -la"


#----------------------------------------------------------------------
# set terminal title including current directory
#----------------------------------------------------------------------
precmd() {
    echo -ne "\033]0;${PWD}\007"
}

#----------------------------------------------------------------------
# Prediction configuration
#----------------------------------------------------------------------
#autoload predict-on
#predict-on

#----------------------------------------------------------------------
# Default Editor is Sublime
#----------------------------------------------------------------------
export EDITOR='atom'


#----------------------------------------------------------------------
# Show branch name in Zsh's right prompt
#----------------------------------------------------------------------
function rprompt-git-current-branch {
        local name st color

        if [[ "$PWD" =~ '/\.git(/.*)?$' ]]; then
                return
        fi
        name=$(basename "`git symbolic-ref HEAD 2> /dev/null`")
        if [[ -z $name ]]; then
                return
        fi
        st=`git status 2> /dev/null`
        if [[ -n `echo "$st" | grep "^nothing to"` ]]; then
                color=${fg[green]}
        elif [[ -n `echo "$st" | grep "^nothing added"` ]]; then
                color=${fg[yellow]}
        elif [[ -n `echo "$st" | grep "^# Untracked"` ]]; then
                color=${fg_bold[red]}
        else
                color=${fg[red]}
        fi

        # %{...%} は囲まれた文字列がエスケープシーケンスであることを明示する
        # これをしないと右プロンプトの位置がずれる
        echo "%{$color%}$name%{$reset_color%} "
}

# プロンプトが表示されるたびにプロンプト文字列を評価、置換する
setopt prompt_subst

RPROMPT='[`rprompt-git-current-branch`%~]'

#----------------------------------------------------------------------
# Prompt color
#----------------------------------------------------------------------
# PROMPT="%{${fg[blue]}%}[%n@%m:%1~] %(!.#.$) %{${reset_color}%}"
# PROMPT="%1~ %(!.#.$) %{${reset_color}%}"
PROMPT="%{${fg_bold[red]}%}→ %{${fg_no_bold[cyan]}%}%1~ %{${reset_color}%}"
PROMPT2="%{${fg[blue]}%}%_> %{${reset_color}%}"
SPROMPT="%{${fg[red]}%}correct: %R -> %r [n,y,a,e]? %{${reset_color}%}"
# RPROMPT="%{${fg[green]}%}[%~]%{${reset_color}%}"

#----------------------------------------------------------------------
# zsh editor
#----------------------------------------------------------------------
# http://opensource.apple.com/source/zsh/zsh-34/zsh/Functions/Misc/zcalc
autoload -U zcalc

autoload -U zed && zed -b
# fix up down keybind in zed (https://sites.google.com/site/codehen/environment/zsh)
bindkey -M zed "^P" up-line-or-search
bindkey -M zed "^N" down-line-or-search
