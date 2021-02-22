import os
filenames = os.listdir()
print(filenames)


with open("index.md", "w") as g:
    g.write("---\nlayout: page\n---\n")
    g.write("<ul>")

    for filename in filenames:
        if filename != "index.md" and filename != "makeindex.py" and filename[0] != "." and filename != "make_pdf.py":
            if "." in filename:
                line = "<li><a href = \"{}\">{}</a></li>\n".format(filename, filename)
                line = line.replace(".md","")
                if filename[0:3] != "PRI":
                    if ".pdf" in filename:
                        if filename.replace(".pdf", ".md") not in filenames:
                            g.write(line)
                    else:
                        g.write(line)


            else:
                line = "<li><a href = \"{}\"><i class=\"material-icons\" style=\"color:#bbb\">folder</i> {}</a></li>\n".format(filename, filename)
                g.write(line)

    g.write("</ul>")
    g.write("<br>")
    g.write("<br>")
    g.write("<a href = \"links\">>> links</a>")
