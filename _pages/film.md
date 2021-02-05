---
title: Film
permalink: /film/
layout: page
---
In addition to research, I am also an independent/freelance film-maker.  All of my publically-available projects are included below.

## Nonfiction
<div>
  {% for doc in site.films %}
    {% if doc.genre == "nonfiction" %}
      <a href="{{ doc.url }}"><h3>{{ doc.title }}</h3></a>
      {{ doc.excerpt }}

      <p style="text-align:center;position:relative;top:-0em;"><a href="{{ doc.url }}"> <i>(read more)</i></a></p>
      {% endif %}
  {% endfor %}
</div>

## Fiction
