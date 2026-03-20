---
layout: default
title: Home
---

# Personal Projects

Latest projects:

<ul>
  <li>
    <a href="https://lbd-sports-attendance.streamlit.app/">Gotham FC Attendance Predictor</a> — Interactive ML tool
  </li>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> — {{ post.date | date: "%B %d, %Y" }}
    </li>
  {% endfor %}
</ul>