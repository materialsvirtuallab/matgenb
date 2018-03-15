---
layout: search
---

# Search
<div id="search-div">
    <form action="/search.html" method="get">
      <input type="text" id="search-box" name="query">
      <input type="submit" class="button" value="Search notebooks">
    </form>
</div>

<ul id="search-results"></ul>

<script>
  window.store = {
    {% for post in site.posts %}
      "{{ post.url | slugify }}": {
        "title": "{{ post.title | xml_escape | lower }}",
        "author": "{{ post.author | xml_escape | lower }}",
        "category": "{{ post.category | xml_escape | lower }}",
        "content": {{ post.content | strip_html | strip_newlines | lower | jsonify }},
        "url": "{{ post.url | xml_escape | lower }}"
      }
      {% unless forloop.last %},{% endunless %}
    {% endfor %}
  };
</script>
<script src="https://unpkg.com/lunr/lunr.js"></script>
<script src="/js/search.js"></script>
