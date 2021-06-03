---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Home
layout: homepage
---
<!--
<div>
<span data-nosnippet>
<div style="margin-left:10%;margin-right:100">
<blockquote>I have known several Jacks, and they all, without exception, were more than usually plain.</blockquote>
<p style = "text-align: center;position:relative;top:-0.75em;margin-left:20px;margin-right:20px;z-index: -1;width:90%"> &mdash; Oscar Wilde's play <i>The Importance of Being Earnest</i></p>
</div>
-->
<!--
<div style = "width:100%;position:relative">
<blockquote>If there is an equation for a curve like a bell, there must be an an equation for one like a bluebell, and if a bluebell, why not a rose?  Do we believe nature is written in numbers?</blockquote>
<p style = "text-align:center;position:relative;top:-0.75em;margin-left:20px;margin-right:20px"> &mdash; Tom Stoppard's play <i>Arcadia</i></p>
</div>

</span>
</div>
-->


<div>


<div class = "profile">



<center>
<img style = "width:85%;margin-bottom:20px;border-radius:50%;" src="/assets/small_banner3.jpg">



</center>


<div style = "margin-bottom:30px">
<ul style="list-style-type:none;display: table;
    margin: 0 auto;
    text-align: left;">
<li>
<span class="fas fa-envelope"></span>&ensp;jack.farrell AT colorado.edu
</li>
<li>
<a href = "/schedule">
<span class="fas fa-calendar-day"></span>&ensp;Schedule</a>
</li>
<li>
<a href = "/assets/CV.pdf">
<span class="fas fa-paperclip"></span>&ensp;CV
</a>
</li>

<li>
<a href = "http://github.com/jfarrellhfx">
<span class="fab fa-github"></span>&ensp;Github
</a>
</li>
</ul>
</div>
</div>


<p>My name is <b>Jack Hollis Farrell</b>, and I am a Ph.D. student in physics at the <i>University of Colorado Boulder</i>, a freelance filmmaker, and a science communicator.
</p>



<!-- don't use the following section for the snippet -->
<span data-nosnippet>


<div style="clear:right"></div>


<p>My <a href = "/science/">research</a> focuses on <i>Condensed Matter Physics</i>, the theoretical physics of materials; this wide field includes some of the theory behind Quantum Computers, Superconductors, and more.  My freelance and independent <a href = "/film/">filmmaking</a> has involved short-form science communication pieces and a long-form research documentary.</p>

<p>I was born in Halifax, Nova Scotia, where I went to high school. In 2017, I moved to Toronto to start university at the <i>University of Toronto</i>, and I graduated in June of 2021.  After that, I moved to Boulder, Colorado to start my Ph.D. at the <i>University of Colorado Boulder</i>.</p>

<p>For detailed information, you can access my <a href = "/assets/CV.pdf">CV</a>.  If you don't need the exhaustive detail, find some highlights and news below!</p>


<h2>Education</h2>
<ul><li>Honors B.Sc. Physics, <i>University of Toronto</i>, 2017&ndash;2021</li>
<li>Ph.D. Physics, <i>University of Colorado Boulder</i>, 2021&ndash;Present</li></ul>

<h2>News</h2>
<ul>
{% for post in site.tags["news"] limit:3 %}
<li><a href = "{{post.url}}"><h4 style="margin-bottom:0px">{{ post.title }}</h4></a>
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