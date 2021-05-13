import os
filenames = os.listdir()


with open("index.md", "w") as g:
    g.write("---\nlayout: page\ntitle: Notes\n---\n")
    g.write("Lately, to help my own organization, I have beent trying to keep all my class, research, and general science and mathematics notes together and 'backed up' online.  In case you find any of it useful or interesting, you can find it here.\n")
    g.write("<ul>")

    for filename in filenames:
        if filename != "index.md" and filename != "makeindex.py" and filename[0] != ".":
            if "." in filename:
                line = "<li><a href = \"{}\">{}</a></li>\n".format(filename, filename)
            else:
                line = "<li><a href = \"{}\"><i class=\"material-icons\" style=\"color:#bbb\">folder</i> {}</a></li>\n".format(filename, filename)
            g.write(line)
    g.write("</ul>")
