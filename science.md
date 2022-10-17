---
title: Research Projects
permalink: /research/
layout: page
full-width: true
---

<hr color = "#bbb">
<br>
<div>
  {% assign projects = (site.research_projects | sort: 'date' | reverse)  %}
  {% for doc in projects %}
      <a href="{{ doc.url }}"><h2>{{ doc.title }}</h2></a>
      {{ doc.excerpt }}
      <div style = "margin-bottom:10em"></div>
  {% endfor %}
</div>
