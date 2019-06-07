from os import path
import os
import FileManager as Fm
import textwrap
from View import View


HEIGHT = 700
WIDTH = 1100

fm = Fm.FileManager(path.join(os.getcwd(), 'input'))

wrapper = textwrap.TextWrapper(width=100)

view = View(fm, wrapper, HEIGHT, WIDTH)

view.init_view()

