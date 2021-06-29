---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Home
layout: homepage
---



<h2>News</h2>
<div class = "row">
{% for post in site.tags["news"] %}
<div class = "three-col">
<a href = "{{post.url}}"><h4 style="margin-bottom:0px">{{ post.title }}</h4></a>
<div style="margin-bottom:1em;font-size:14px"><i>{{ post.date | date: "%-d %B %Y" }}</i></div>
{{ post.excerpt }}
<!--<p style="font-size:14px;text-align:center;position:relative;top:-0.5em;"><a href="{{ post.url }}"> <i>(read more)</i></a></p>-->
</div>
{% endfor %}
</div>
<!--
## More about Me
### Science
I am interested in *Condensed Matter Physics* on the theoretical side.  I got into physics in high school by reading lots of so-called "popular" books on the subject.  You can find a list of my favourites here.

### Filmmaking
 I've been making movies with my friends since around middle school.  For the past few years, in addition to my creative film projects, I have been exploring documentary and nonfiction filmmaking.  Lots of examples are on the <a href = "/film/">film</a> page.

### Other Interests
- *Comics:* I am a big fan of comic books and comic book movies.  There are lots of great stores in Toronto.  My "pull file" is set up at The Beguiling in toronto.  This is a great.  If you're interested for some reason, feel free to check out my (usually updated) list of books I'm following right now!
-->
