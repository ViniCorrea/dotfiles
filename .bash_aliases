# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=always'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=always'
    alias fgrep='fgrep --color=always'
    alias egrep='egrep --color=always'
fi

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

alias ps='ps auxf'
alias cls='clear'
alias c='clear'

######################
##### ls aliases #####
######################
# -a: do not ignore entries starting with .
# -l: long list
# -h: human readable sizes like 1k 234M 2G etc
# -t: sort by tume, newest first
# -C: list entries by columns
alias ll='ls -laht'
alias la='ls -A'
alias l='ls -CF'
alias lf="ls -l | egrep -v '^d'" # files only
alias ldir="ls -l | egrep '^d'" # directories only

# Check free space on disks
alias df='df -h'

# Safe operations with files
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

######################
######### cd #########
######################
alias home='cd ~'
alias cd..='cd ..'
alias ..='cd ..;pwd'
alias ...='cd ../..;pwd'
alias ....='cd ../../..;pwd'
# cd into the old directory
alias bd='cd "$OLDPWD"'

#alias tree='tree --dirsfirst -F'
alias tree="find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"


alias mkdir='mkdir -p -v'

###########################
## Other helpful aliases ##
###########################

alias jan='cal -m 01'
alias feb='cal -m 02'
alias mar='cal -m 03'
alias apr='cal -m 04'
alias may='cal -m 05'
alias jun='cal -m 06'
alias jul='cal -m 07'
alias aug='cal -m 08'
alias sep='cal -m 09'
alias oct='cal -m 10'
alias nov='cal -m 11'
alias dec='cal -m 12'

function hg() {
    history | grep "$1";
}

# Shortcuts to vimrc and bashrc
alias vimrc='vim ~/.vimrc'
alias bashrc='vim ~/.bash_profile'
alias loadbash='source ~/.bash_profile'

# A really simple password generator
alias pw='bash -c '"'"'echo `tr -dc $([ $# -gt 1 ] && echo $2 || echo "A-Za-z0-9") < /dev/urandom | head -c $([ $# -gt 0 ] && echo $1 || echo 30)`'"'"' --'

# Show all logs in /var/log
alias logs="sudo find /var/log -type f -exec file {} \; | grep 'text' | cut -d' ' -f1 | sed -e's/:$//g' | grep -v '[0-9]$' | xargs tail -f"
