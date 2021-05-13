import os
from pandas import read_csv
from glob import glob


info = read_csv("all_files.txt")

for n in range(info.shape[0]):
    path = str(info["path"][n])
    name = str(info["name"][n])

    filename = path + name
    print(filename)
    os.makedirs(os.path.dirname(filename), exist_ok = True)

directories = [x[0] for x in os.walk("Notes")]





for directory in directories:
    g = open(directory + "\\" + "index.md", 'w')
    title = os.path.basename(directory)
    g.write("---\nlayout: page\ntitle: {}\n---\n".format(title))


    g.write("<h3><span class=\"material-icons\" style=\"position:relative;top:0.1em\">folder</span>&ensp;Folders</h3>")
    g.write("<ul>\n")

    names = os.listdir(directory)
    for foldername in names:
        if foldername != "index.md":
            line = "<li><a href = \"{}\"><i class=\"material-icons\" style=\"position:relative;top:0.2em\">folder</i>&ensp;{}</a></li>\n".format(foldername, foldername)
            g.write(line)


    g.write("</ul>")
    g.close()

for directory in directories:

    title = os.path.basename(path)
    g = open(directory + "\\" + "index.md", 'a')

    g.write("<h3><span class=\"material-icons\" style=\"position:relative;top:0.1em\">description</span>&ensp;Files</h3>\n")
    g.write("<ul>\n")
    g.close()


for n in range(info.shape[0]):
    path = str(info["path"][n])
    name = str(info["name"][n])
    url = str(info["url"][n])
    starred = float(info["starred"][n])



    if name != "index.md" and filename[0] != "." and filename != "make_pdf.py" and filename != "links":

        if starred:
            line = "<li><div style = \"color:LightCoral\">{}</div></li>".format(name)
        else:
            line = "<li><a href = \"{}\">{}</a></li>\n".format(url, name)
        g = open(path + "/" + "index.md", 'a')
        g.write(line)
        g.close()


for directory in directories:
    g = open(directory + "/" + "index.md", 'a')
    g.write("</ul>\n")
    g.close()

for directory in directories:
    g = open(directory + "/" + "index.md", 'a')

    g.write("<h3><span class=\"material-icons\" style=\"position:relative;top:0.1em\">link</span>&ensp;Links</h3>")
    g.write("<ul>\n")

    g.close()

links = read_csv("all_links.txt")
print(links)

for n in range(links.shape[0]):
    url = links["url"][n]
    path = links["path"][n]

    g = open(path + "index.md", 'a')
    g.write("<li><a href = \"{}\">{}</a></li>\n".format(url,url))
    g.close()
for directory in directories:
    g = open(directory + "/" + "index.md", 'a')
    g.write("</ul>")
    g.close()
