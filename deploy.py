#coding=utf-8
#!/usr/bin/python

import subprocess
from subprocess import Popen,PIPE,STDOUT 

def exec_shell(cmd):
		proc = subprocess.Popen(cmd,shell=True)
		return proc.communicate()

print exec_shell("git clone http://github.com/gmarik/vundle.git ~/.vim/bundle/vundle.vim");
print exec_shell("cp .vimrc ~/");
print exec_shell("vim +PluginInstall +qall");
