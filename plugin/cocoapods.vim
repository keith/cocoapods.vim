" File: cocoapods.vim
" Author: Keith Smiley
" Description: General file configuration for CocoaPods within vim
" Last Modified: April 26, 2014

if exists("g:loaded_cocoapods") && g:loaded_cocoapods
  finish
endif
let g:loaded_cocoapods = 1

augroup ft_podspec
  autocmd!
  autocmd BufNewFile,BufRead,BufWrite *.podspec setlocal filetype=podspec
  autocmd BufNewFile,BufRead Podfile setlocal filetype=podfile

  autocmd FileType podspec,podfile set syntax=ruby
  autocmd FileType podspec,podfile set commentstring=#%s
  autocmd FileType podspec compiler cocoapods
  autocmd FileType podfile setlocal makeprg=pod\ install\ >/dev/null
augroup END
