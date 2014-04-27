autocmd BufNewFile,BufRead Podfile setlocal filetype=podfile
autocmd FileType podfile setlocal syntax=ruby
autocmd FileType podfile setlocal commentstring=#%s
autocmd FileType podfile setlocal makeprg=pod\ install
