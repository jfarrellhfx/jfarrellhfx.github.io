---
title: Film
permalink: /film/
layout: page
full-width: true
order: 1
---
<hr color = "#bbb">
<br>
<div>

<div>
  {% assign films = (site.films | sort: "order") %}
  {% for doc in films %}
      <a href="{{ doc.url }}"><h2>{{ doc.title }}</h2></a>
      {{ doc.excerpt }}
      <div style = "margin-bottom:10em"></div>
  {% endfor %}
</div>
