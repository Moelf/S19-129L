set number 
set autoindent
set smartindent
set nowrap
set ruler
set ignorecase
set hlsearch
set incsearch
set showmatch
set foldmethod=syntax
set foldlevel=9
set pastetoggle=<F2>
set expandtab
set updatetime=100
set smarttab
set shiftwidth=4
set tabstop=4
set nowrap
set clipboard+=unnamedplus
set termguicolors
syntax enable
filetype plugin indent on
"open file under cursor in v split
autocmd FileType python nnoremap <buffer> <C-p> :w<CR>:exec '!python' shellescape(@%,1)<CR>
" set a directory to store the undo history
set undofile
set undodir=~/.vimundo/
