---
title: Film
permalink: /film/
layout: page
---

In addition to research, I am also an independent/freelance film-maker.  All of my publically-available projects are included below.
<div class = "sidebar">
<div class = "profchild">
<h3>Navigation</h3>
<ul>
<li><a href = "#nonfiction">Nonfiction</a></li>
<li><a href = "#fiction">Fiction</a></li>
</ul>
</div>
</div>

<h2 id = "nonfiction">Nonfiction</h2>
<div>
  {% for doc in site.films %}
    {% if doc.genre == "nonfiction" %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
      <p style="text-align:center;position:relative;top:-1em;"><a href="{{ doc.url }}"> <i>(read more)</i></a></p>
      {% endif %}
  {% endfor %}
</div>

<h2 id = "fiction">Fiction</h2>
<div>
  {% for doc in site.films %}
    {% if doc.genre == "fiction" %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
      <p style="text-align:center;position:relative;top:-1em;"><a href="{{ doc.url }}"> <i>(read more)</i></a></p>
      {% endif %}
  {% endfor %}
</div>
