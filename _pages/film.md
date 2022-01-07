---
title: Film
permalink: /film/
layout: page
---

In addition to research, I am also an independent/freelance film-maker.  All of my publically-available projects are included below.

<h2>Nonfiction</h2>
<div>
  {% for doc in site.films %}
    {% if doc.genre == "nonfiction" %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
      {% endif %}
  {% endfor %}
</div>

<h2>Fiction</h2>
<div>
  {% for doc in site.films %}
    {% if doc.genre == "fiction" %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}
      {% endif %}
  {% endfor %}
</div>
