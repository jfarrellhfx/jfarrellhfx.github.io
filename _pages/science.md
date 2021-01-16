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

## Math and Physics Notes

In this section, I document the collection of miscellaneous notes on mathematics and physics.  Some of them are large exposition (or documents of my self-study), while some are short explanations of mathematical tricks or trivia.

<div>
{% assign subjects = site.notes | group_by:"subject" %}
{% for subject in subjects %}
    <h3>{{ subject.name }}</h3>
    <ul>
    {% for item in subject.items %}
    <li> <a href="{{ item.url }}"><h4>{{ item.title }}</h4></a>
    {% unless item.show_excerpt == false %}
    {{ item.excerpt }}
    {% endunless %}

    </li>

    {% endfor %}
    </ul>
{% endfor %}
</div>
