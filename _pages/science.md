---
title: Science
permalink: /science/
layout: page
---


## Past Research Projects

I am interested in the theoretical physics of materials, called *Condensed Matter Physics*.  You can read about my recent research projects, in this area and others, below.


<div>
  {% assign projects = (site.research_projects | sort: "order") %}
  {% for doc in projects %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
      <p style="text-align:center;position:relative;top:-0em;"><a href="{{ doc.url }}"> <i>(read more)</i></a></p>
  {% endfor %}
</div>

## Technical Writing
### Unpublished
- <a href = "/tech_writing/variational_report.pdf"><i>A Variational Monte Carlo Method for the Schrodinger Equation</i></a><br>Final report for the course PHY 407 taught by Nicolas Grisouard at the University of Toronto, taken in fall 2020.  <a href = "https://github.com/jfarrellhfx/variational-monte-carlo">GitHub Repo</a>.
