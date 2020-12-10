import os
import sys

filename = sys.argv[1]
name, ext = os.path.splitext(filename)

with open(filename, "r") as f:
    contents = f.read()
    new_contents = contents.replace("$$\\", "\\")
    new_contents = new_contents.replace("}$$", "}")

new_filename = "intermed_" + filename

with open(new_filename, 'w') as g:
    g.write(new_contents)

os.system("pandoc -s {} -o {}.pdf".format(new_filename, name))
os.remove(new_filename)
