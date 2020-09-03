""" Plugins """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Vim-plug.
" Automatic installation (https://github.com/junegunn/vim-plug/wiki/tips#automatic-installation)
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif
call plug#begin('~/.vim/plugged')
Plug 'Valloric/YouCompleteMe', { 'do': '/usr/bin/python ./install.py --clang-completer' } " Code completion, syntax checking
Plug 'altercation/vim-colors-solarized'                                   " Colors
Plug 'scrooloose/nerdtree'                                                " Folder navigation
Plug 'tpope/vim-fugitive'                                                 " Git tools
Plug 'majutsushi/tagbar'                                                  " Local source structure
Plug 'vim-airline/vim-airline'                                            " Status bar
Plug 'vim-airline/vim-airline-themes'
Plug 'godlygeek/Tabular'                                                  " Alignment (Try :Tab /=)
Plug 'tmhedberg/simpylfold'                                               " Python folding
call plug#end()

" YouCompleteMe
" Note: if you want to search header files for completions, type <c-Space>
" Troubleshooting: sometimes one needs to delete .vim/plugged/YouCompleteMe
"                  and re-run :PlugInstall
let g:ycm_confirm_extra_conf = 0                                          " unsafe!
let g:ycm_global_ycm_extra_conf = "~/util/rc/ycm_extra_conf.py"
let g:ycm_autoclose_preview_window_after_completion = 1
let g:ycm_always_populate_location_list = 1

" On OS X, YCM insists on using system Python
if has("unix")
  let s:uname = system("uname")
  if s:uname == "Darwin\n"
    let g:ycm_path_to_python_interpreter = '/usr/bin/python'
  endif
endif

" Airline
let g:airline_theme='solarized'
let g:airline_solarized_bg='dark'
let g:airline_mode_map = {
    \ '__' : '-',
    \ 'c'  : 'C',
    \ 'i'  : 'I',
    \ 'ic' : 'I',
    \ 'ix' : 'I',
    \ 'n'  : 'N',
    \ 'ni' : 'N',
    \ 'no' : 'N',
    \ 'R'  : 'R',
    \ 'Rv' : 'R',
    \ 's'  : 'S',
    \ 'S'  : 'S',
    \ '' : 'S',
    \ 't'  : 'T',
    \ 'v'  : 'V',
    \ 'V'  : 'V',
    \ '' : 'V',
    \ }

""" Behavior """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Disable ex mode
nnoremap Q <nop>

" Turn on mouse scrolling/selecting (works in iTerm2)
:set mouse=a

" Backspace beyond current insert (probably a bad habit)
set backspace=indent,eol,start

" 2 spaces instead of tabs
set expandtab
set tabstop=2
set softtabstop=2
set shiftwidth=2

" Smart case handling for searches
set ignorecase
set smartcase

" Indentation
set autoindent

" Search while typing, highlight matches
set incsearch
set hlsearch

" Change tab completion to be bash-like
set wildmode=longest,list

" Default tags to PETSc ctags
set tags=$PETSC_DIR/CTAGS

" Folding
let fortran_fold=1
let fortran_fold_conditionals=1
set fdm=syntax
set foldlevelstart=99 " this seems like a hack

" Disable automatic multiline commenting
autocmd BufNewFile,BufRead * setlocal formatoptions-=cro

""" Appearance """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Line numbers
set number

" Syntax highlighting and color scheme
syntax on
colorscheme solarized
set background=dark
let fortran_free_source=1

" Spellchecking highlighting
hi clear SpellBad
hi SpellBad cterm=bold ctermfg=white ctermbg=red
hi SpellBad gui=bold guifg=white guibg=red

" Use C syntax highlighting for additional extensions
autocmd BufNewFile,BufRead *.cl   set syntax=c

" Color column in active window
set colorcolumn=81
augroup BgHighlight
    autocmd!
    autocmd WinEnter * set colorcolumn=81
    autocmd WinLeave * set colorcolumn=0
augroup END

""" Shortcuts """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Unset the "last search pattern" register
nnoremap <CR> :noh<CR><CR>

" Copy to system clipboard, if supported
map <F2> "*y

" Kill all trailing whitespace (undo to leave highlighted)
nmap <F3> :%s/\s\+$//<CR>

" Jump to tag, in new window
nmap <F7> :vsp<CR><c-w><c-l><c-]>

" Tagbar
nmap <F8> :TagbarToggle<CR>

" Jump to next in location list, wrapping (for YouCompleteMe)
command Lnextwrap try | lnext | catch | lfirst | catch | endtry
nmap <F11> :Lnextwrap<CR>

" YouCompleteMe FixIt
nmap <F12> :YcmCompleter FixIt<CR>

" Move between windows
nnoremap <c-h> <c-w>h
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-l> <c-w>l

" Next/prev tab
nnoremap <TAB> gt
nnoremap <S-TAB> gT

" PETSc
imap <c-\>ch CHKERRQ(ierr);
imap <c-\>po PetscObjectComm((PetscObject)dm)
imap <c-\>pe SETERRQ(PetscObjectComm((PetscObject)dm),PETSC_ERR_SUP,"Not Implemented!");
imap <c-\>pp ierr = PetscPrintf(PETSC_COMM_WORLD,"xxx\n");CHKERRQ(ierr);
imap <c-\>pf PetscErrorCode XXXX()<CR>{<CR>PetscErrorCode ierr;<CR><CR>PetscFunctionBegin;<CR>PetscFunctionReturn(0);<CR>}<CR>

" use "open" (OS X) to open a filename under the cursor
" The second <CR> means that you won't get to read error messages,
" but also won't have to press enter again to return to the file in vim
nnoremap Gf :!open <cWORD> <CR> <CR>
