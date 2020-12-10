---
title: Writing
permalink: /writing/
layout: page
---
This page is meant to give an overview of my writing.  If you'd rather see the notes and articles organized by category, p lease feel free to visit the [archive](/archive) page!


## Math and Physics Notes

This is where you can find my collection of notes (some more technical than others) on a variety of topics in mathematics and physics. The notes are consistently updated, they may (read: definitely) contain errors. *In most cases, you can also download a `pdf` of the notes by by clicking a button at the end of each page*. 

<details><summary>View Notes</summary>
<div>
{% assign subjects = site.notes| group_by:"subject" %}
{% for subject in subjects %}
    <h3>{{ subject.name }}</h3>
    <ul>
    {% for item in subject.items %}
    <li> <a href="{{ item.url }}"><div style="font-family: Roboto;font-size:14pt">{{ item.title }}</div></a>
    {{ item.excerpt }}
    </li>

    {% endfor %}
    </ul>
{% endfor %}
</div>
</details>


## Blog

<ul>
  {% for post in site.categories.Other %}

     <li> <a href="{{ post.url }}"><div style="font-family: Roboto;font-size:16pt">{{ post.title }}</div></a>
      {{ post.excerpt }}
      <div style="text-align:right;position:relative;top:-1em;"><i>
({{ post.date | date: '%d %B, %Y' }})</i></div>
</li>
  {% endfor %}
</ul>
