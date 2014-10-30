set nocompatible
filetype off
"inoremap { {}<Left>
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Bundle 'klen/python-mode'
Bundle 'davidhalter/jedi-vim'
Bundle 'ervandew/supertab'
set guifont=DejaVu\ Sans\ Mono\ for\ Powerline\ 9
set laststatus=2
call vundle#end()
filetype plugin indent on
let g:pymode_rope = 0
let g:pymode_link = 1
let g:pymode_lint_checker= 'pyflakes,pep8'
let g:pymode_lint_write = 1
let g:pymode_breakpoint = 1
let g:pymode_breakpoint_ley = '<leader>b'
let g:pymode_syntax = 1
let g:pymode_syntax_all = 1
let g:pymode_syntax_indent_errors = g:pymode_syntax_all
let g:pymode_syntax_space_errors = g:pymode_syntax_all
let g:pymode_folding = 0
let g:SuperTabDefaultCompletionType = '<c-n>'
