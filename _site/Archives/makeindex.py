import os
filenames = os.listdir()


with open("index.md", "w") as g:
    g.write("---\nlayout: page\n---\n")
    g.write("<ul>")

    for filename in filenames:
        if filename != "index.md" and filename != "makeindex.py":
            line = "<li><a href = \"{}\">{}</a></li>\n".format(filename, filename)
            g.write(line)
    g.write("</ul>")
