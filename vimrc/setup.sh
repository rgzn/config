#!/usr/bin/env sh
# Symlink settings files into the appropriate place.

PSANAN_RC_ROOT=$HOME/util/rc
LINK="ln -sf" # WARNING: will clobber

$LINK $PSANAN_RC_ROOT/profile      $HOME/.profile
$LINK $PSANAN_RC_ROOT/bash_profile $HOME/.bash_profile
$LINK $PSANAN_RC_ROOT/bashrc       $HOME/.bashrc

$LINK $PSANAN_RC_ROOT/gdbinit      $HOME/.gdbinit
$LINK $PSANAN_RC_ROOT/latexmkrc    $HOME/.latexmkrc
$LINK $PSANAN_RC_ROOT/octaverc     $HOME/.octaverc
$LINK $PSANAN_RC_ROOT/screenrc     $HOME/.screenrc

mkdir -p $HOME/.vim/after/indent
mkdir -p $HOME/.vim/spell
$LINK $PSANAN_RC_ROOT/vimrc                       $HOME/.vimrc
$LINK $PSANAN_RC_ROOT/vim/after/indent/python.vim $HOME/.vim/after/indent/python.vim
$LINK $PSANAN_RC_ROOT/vim/spell/en.utf-8.add      $HOME/.vim/spell/en.utf-8.add

mkdir -p $HOME/.config/yapf
$LINK $PSANAN_RC_ROOT/config/yapf/style           $HOME/.config/yapf/style
