autocmd BufNewFile,BufRead,BufWrite *.podspec setlocal filetype=podspec
autocmd FileType podspec setlocal syntax=ruby
autocmd FileType podspec setlocal commentstring=#%s
autocmd FileType podspec compiler cocoapods
