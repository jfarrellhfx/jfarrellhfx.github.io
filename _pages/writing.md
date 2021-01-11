---
title: Writing
permalink: /writing/
layout: page
---
This page is meant to give an overview of my writing.  If you'd rather see the notes and articles organized by category, p lease feel free to visit the [archive](/archive) page!


## Math and Physics Notes

When I am trying to learn a concept, it helps a lot to write it out as if I am explaining it to myself.  These notes are part of that exercise.  Here, you can find pages (some more technical than others) on a variety of topics in mathematics and physics. The notes are consistently updated; they may (read: definitely) contain errors. *In most cases, you can also download a `pdf` of the notes by by clicking a button at the end of each page*.

<div>
{% assign subjects = site.notes | group_by:"subject" %}
{% for subject in subjects %}
    <h3>{{ subject.name }}</h3>
    <ul>
    {% for item in subject.items %}
    <li> <a href="{{ item.url }}"><h4>{{ item.title }}</h4></a>
    {{ item.excerpt }}
    </li>

    {% endfor %}
    </ul>
{% endfor %}
</div>


## Blog Highlights
