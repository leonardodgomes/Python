#Get the folder path and file name

import pathlib
print("--------Using pathlib.Path().absolute(): ")
print(pathlib.Path().absolute())


from pathlib import Path
print("--------Using Path.cwd(): ")
print(Path.cwd())


import os
print("--------Using OS ")
print('File name :    ', os.path.basename(__file__))
print('Directory Name:     ', os.path.dirname(__file__))

