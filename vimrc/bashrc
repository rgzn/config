# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# Note: for some remote machines, we may have another bashrc, which sources this

### Location for additional scripts ############################################
PSANAN_RC_ROOT=${PSANAN_RC_ROOT:-$HOME/util/rc}

### Terminal ###################################################################
export CLICOLOR=1;                  # colorize the terminal
export HISTCONTROL=ignoredups       # include commands starting with a space

### Aliases and helper functions ###############################################
alias gg="git grep"
alias lg="lazygit"
alias ll="ls -l"
alias mj="make -j8"
alias sb="source $HOME/.bashrc"
alias cdn="cd $HOME/work/notes/notes"
alias cdt="cd $HOME/work/notes/tech"
alias dus="du -sh * | sort -hr"
alias vimr="vim -R"
alias news="newsboat"
alias plab="ipython --no-confirm-exit --matplotlib -i $HOME/code/petsc_python_helpers/ipython_setup.py"

function t {
  d=`date +%Y.%m.%d`
  note_path_stem="$HOME/work/notes/tech/$d"
  note_path=$(printf '%s.md' "$note_path_stem")
  i=0
  while [ -f "$note_path" ]
  do
    ((i++))
    note_path=$(printf '%s_%d.md' "$note_path_stem" $i)
  done
  printf '# Untitled Tech Note\n' >> $note_path
  printf '{tag1} {tag2}\n'        >> $note_path
  vim $note_path
}

### Git ########################################################################
git config --global user.name "Patrick Sanan"
git config --global user.email "patrick.sanan@gmail.com"
git config --global color.status auto
git config --global color.branch auto
git config --global push.default tracking
git config --global core.editor vim

alias  gitl="git log --graph --pretty=format:\"%h - %an, %ar : %s %d\""
alias  gits="git status --short"
alias gitst="git status --short --untracked-files=no"

source $PSANAN_RC_ROOT/git-completion.bash
source $PSANAN_RC_ROOT/git-prompt.sh
GIT_PS1_SHOWUPSTREAM=true
GIT_PS1_SHOWDIRTYSTATE=true
GIT_PS1_SHOWSTASHSTATE=true
GIT_PS1_SHOWUNTRACKEDFILES=true

### Prompt #####################################################################
# addsp adds a space and (optional) brackets to non-empty strings
# Don't forget the \[ \], or you'll have line-wrapping issues
# $STY is for use with GNU Screen (screen -S sessionName)
function addsp { if [[ -z "$1" ]]; then echo ""; else echo "$2$1$3 "; fi; }
PS1_OPEN="\[\e[1;31m\]["
PS1_CLOSE="\[\e[1;31m\]]$\[\e[0m\] "
PS1_BODY='\[\e[0;34m\]$(addsp "$STY")\[\e[0;95m\]$(addsp "$PETSC_ARCH" "(" ")")\[\e[1;31m\]\W\[\e[0;36m\]$(__git_ps1 " (%s)")'
PS1_HOST="\[\e[0;33m\]\H "
PS1_LOCAL="$PS1_OPEN$PS1_BODY$PS1_CLOSE"
PS1_REMOTE="$PS1_OPEN$PS1_HOST$PS1_BODY$PS1_CLOSE"
PS1=$PS1_REMOTE

### PETSc and related software #################################################
alias cdp='cd $PETSC_DIR'                                   # note single quotes
alias cdk='cd $PETSC_DIR/src/ksp/ksp/tutorials'
alias cdd='cd $PETSC_DIR/src/dm/impls/stag/tutorials'

function whichp {
                                echo -n 'PETSC_ARCH = '; echo $PETSC_ARCH
                                echo -n 'PETSC_DIR  = '; echo $PETSC_DIR
                                echo -n 'PMPI       = '; echo $PMPI
  if [ -n "$SLEPC_DIR"  ]; then echo -n 'SLEPC_DIR  = '; echo $SLEPC_DIR;  fi
  if [ -n "$PTATIN_DIR" ]; then echo -n 'PTATIN_DIR = '; echo $PTATIN_DIR; fi
  if [ -n "$LAMEM_DIR"  ]; then echo -n 'LAMEM_DIR  = '; echo $LAMEM_DIR;  fi
  if [ -n "$PETSC_DEB"  ]; then echo -n 'PETSC_DEB  = '; echo $PETSC_DEB;  fi #for LaMEM
  if [ -n "$PETSC_OPT"  ]; then echo -n 'PETSC_OPT  = '; echo $PETSC_OPT;  fi #for LaMEM
}

alias unsetp='unset PETSC_ARCH PETSC_DIR PMPI PETSC_DEB PETSC_OPT'
alias confp='grep CONFIGURE_OPTIONS $PETSC_DIR/$PETSC_ARCH/lib/petsc/conf/petscvariables'

# Functions to set common PETSc configurations.
# See petsc_configure*.sh in the petsc_configure_helpers repo
function space2dash {
  # Concatenate arguments and replace spaces with dashes
  echo "$@" | sed 's/ /-/g'
}
function setp {
  # Usage: setp <archmod> [<precision> <extra> ... ] <debug/opt>
  # Example: setp 3.7 extra opt
  #          --> PETSC_ARCH=arch-3.7-extra-opt, PETSC_DIR=$HOME/code/petsc-3.7
  local ARCHMOD=$1
  local MOREMODS=$(space2dash ${@:2})
  export PETSC_DIR=$HOME/code/petsc-$ARCHMOD
  export PETSC_ARCH=arch-$ARCHMOD-$MOREMODS
  export PMPI=$PETSC_DIR/lib/petsc/bin/petscmpiexec
}
function setpprefix {
  # Usage: setpprefix <archmod> <precision-extra-opt-etc>
  local ARCHMOD=$1
  local MOREMODS=$(space2dash ${@:2})
  export PETSC_DIR=$HOME/code/petsc-$ARCHMOD/arch-$ARCHMOD-$MOREMODS-install
  unset PETSC_ARCH
  export PMPI=$PETSC_DIR/lib/petsc/bin/petscmpiexec
}
function setphere {
  # Usage: setphere <petsc-arch>
  # Example: cd /some/petsc/dir && setphere arch-foo-bar
  export PETSC_DIR=$PWD
  export PETSC_ARCH=${1%/} # strip any trailing slash, so you can tab-complete
  export PMPI=$PETSC_DIR/lib/petsc/bin/petscmpiexec
}

# LaMEM
function lamemhelper {
  # Usage: lamemhelper <archmod>
  local ARCHMOD=${1:-maint}
  export PETSC_DEB=$HOME/code/petsc-$ARCHMOD/arch-$ARCHMOD-extra-debug-install
  export PETSC_OPT=$HOME/code/petsc-$ARCHMOD/arch-$ARCHMOD-extra-opt-install
  export PETSC_DIR=$PETSC_OPT
  export PMPI=$PETSC_OPT/bin/mpiexec
  unset PETSC_ARCH
  export LAMEM_DIR=$HOME/code/lamem-$ARCHMOD
  whichp
}
alias lamemtest='cd $LAMEM_DIR/input_models/BuildInSetups; ../../bin/opt/LaMEM -ParamFile FallingBlock_DirectSolver.dat'
alias lamemtest2='cd $LAMEM_DIR/input_models/BuildInSetups; $PMPI -np 2 ../../bin/opt/LaMEM -ParamFile FallingBlock_DirectSolver.dat'

### Linux-specific commands ####################################################
if [[ "$OSTYPE" == "linux-gnu" ]]; then

# Paraview
alias paraview="~/ParaView-5.6.0-MPI-Linux-64bit/bin/paraview"

fi # Linux

### OS X-specific commands ####################################################
if [[ "$OSTYPE" == "darwin"* ]]; then

# Use "local prompt"
PS1=$PS1_LOCAL

# Vim and MacVim: check that the expected symlinks exist
# (If this isn't true, YouCompleteMe will experience strange crashes)
vim_symlink='/usr/local/bin/vim'
vim_symlink_target='/Applications/MacVim.app/Contents/bin/vim'
if [ ! -e "$vim_symlink" -o "$(readlink $vim_symlink)" != "$vim_symlink_target" ]; then
    printf "WARNING: $vim_symlink does not link to $vim_symlink_target as expected!\n"
    printf "Perhaps you want to do this:\n"
    printf "    sudo ln -s $vim_symlink_target $vim_symlink\n"
fi
alias vi="echo use vim"

# Paraview
alias paraview="/Applications/ParaView-5.6.0.app/Contents/MacOS/paraview"

# Ideatron
alias iii="$HOME/code/ideatron/run.py -d $HOME/docs/ideatron_local"

# Helpers
source $HOME/.helpers.sh

fi # OS X
