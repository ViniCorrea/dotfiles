if ! command -v yay &> /dev/null
then
    echo "[yay] could not be found"
    exit
fi
yay -Sq --nodiffmenu --noeditmenu --nouseask --nocleanmenu --noupgrademenu awk

git clone --bare https://github.com/ViniCorrea/dotfiles.git $HOME/.cfg
function dotfiles {
   /usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME $@
}
mkdir -p .dotfiles-backup
dotfiles checkout
if [ $? = 0 ]; then
  echo "Checked out config.";
  else
    echo "Backing up pre-existing dot files.";
    dotfiles checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} .dotfiles-backup/{}
fi;
dotfiles checkout
dotfiles config status.showUntrackedFiles no


sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --keep-zshrc --unattended
yay -Sq --nodiffmenu --noeditmenu --nouseask --nocleanmenu --noupgrademenu nerd-fonts-complete
sh -c "$(curl -fsSL https://starship.rs/install.sh)" "" --yes 
yay -Sq  --nodiffmenu --noeditmenu --nouseask --nocleanmenu --noupgrademenu neofetch rofi kitty xrandr nitrogen
exec zsh -l