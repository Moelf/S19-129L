Using python 3.5.3
list of modules and their versions can be found in module_list.txt

* installation of iminuit is needed for this hw, 
this is most easily done by `pip install iminuit --user` to avoid permission 
issue *

* For all problems, just run 'python3 exer*.py' where * is the problem number. *
Required outputs should be print to the terminal emulator, or draw to graphical
output through matplotlib, or through interaction prompt.


exer1
-------------------------------------------------------------------------------
Check ./exer1.pdf for hacky code and nice plots and ./exer1.py for acutaly
code and comments.

Used files are from ./ccHistStuff.py ./mass.txt

exer2
-------------------------------------------------------------------------------
`python3 exer1.py` would result in a `data.pik` file in the current directory,
notice you want to run this in the directory where `mass.txt` exists.
Then check sanity with `python3 checkDecayChain.py` and profit :D

P.S:
./ccHistStuff.py contains Claudio's stat box class (with modifictaion)
./LVector.py contains the provied solution to HW 6
