---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Home
layout: no_title_page
---
<div>
<span data-nosnippet>
<blockquote>I have known several Jacks, and they all, without exception, were more than usually plain. Besides, Jack is a notorious domesticity for John! And I pity any woman who is married to a man called John.</blockquote>
<p style = "text-align: center;position:relative;top:-0.75em;margin-left:20px;margin-right:20px"> &mdash; Oscar Wilde's play <i>The Importance of Being Earnest</i></p>

<blockquote>Each week I plot your equations dot for dot, <i>x</i>s against <i>y</i>s in all manner of algebraical relation, and every week they draw themselves as commonplace geometry, as if the world of forms were nothing but arcs and angles.  God’s truth, Septimus, if there is an equation for a curve like a bell, there must be an an equation for one like a bluebell, and if a bluebell, why not a rose?  Do we believe nature is written in numbers?</blockquote>
<p style = "text-align:center;position:relative;top:-0.75em;margin-left:20px;margin-right:20px"> &mdash; Tom Stoppard's play <i>Arcadia</i></p>
</span>
</div>



# Welcome!
<img class = "responsive" src = "/assets/farrellJPG.JPG">
My name is Jack Hollis Farrell, and I am an undergraduate student at the University of Toronto studying physics.  Mostly, I am interested in *Condensed Matter Physics*, the theoretical physics of materials --- this wide field includes some of the theory behind Quantum Computers, Superconductors, and more.

I was born in Halifax, Nova Scotia, where I went to high school. In 2017, I moved to Toronto to start university, and I plan to graduate in June of 2021.




## News
<ul>
{% for post in site.tags["news"] limit:3 %}
<li><a href = ""><h4 style="margin-bottom:0px">{{ post.title }}</h4></a>
<div style="margin-bottom:1em;font-size:14px"><i>{{ post.date | date: "%-d %B %Y" }}</i></div>
{{ post.content }}
</li>
{% endfor %}
</ul>


<!--
## More about Me
### Science
I am interested in *Condensed Matter Physics* on the theoretical side.  I got into physics in high school by reading lots of so-called "popular" books on the subject.  You can find a list of my favourites here.

### Filmmaking
 I've been making movies with my friends since around middle school.  For the past few years, in addition to my creative film projects, I have been exploring documentary and nonfiction filmmaking.  Lots of examples are on the <a href = "/film/">film</a> page.

### Other Interests
- *Comics:* I am a big fan of comic books and comic book movies.  There are lots of great stores in Toronto.  My "pull file" is set up at The Beguiling in toronto.  This is a great.  If you're interested for some reason, feel free to check out my (usually updated) list of books I'm following right now!
-->
