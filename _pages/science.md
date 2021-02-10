---
title: Science
permalink: /science/
layout: page
---



## Research Projects

I am interested in the theoretical physics of materials, called *Condensed Matter Physics*.  You can read about my recent research projects, in this area and others, below.


<div>
  {% assign projects = (site.research_projects | sort: "order") %}
  {% for doc in projects %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
      <p style="text-align:center;position:relative;top:-0em;"><a href="{{ doc.url }}"> <i>(read more)</i></a></p>
  {% endfor %}
</div>

## Virtual Lab Book

Lately, to help my own organization, I have beent trying to keep all my class, research, and general science and mathematics notes together and 'backed up' online.  In case you find any of it useful or interesting, you can find it <a href = "/labbook">here</a>.
