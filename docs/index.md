---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
---

This website is started by the [Materials Virtual Lab](http://www.materialsvirtuallab.org) as a useful collection of Jupyter notebooks that demonstrate the utilization of open-source codes for the study of materials science.

We frequently get requests (from students, postdocs, collaborators, or just general users) for example codes that demonstrate various capabilities in the open-source software we maintain and contribute to, such as the Materials Project software stack comprising [Python Materials Genomics (pymatgen)](http://www.pymatgen.org), [Custodian](https://materialsproject.github.io/custodian/), and [Fireworks](https://pythonhosted.org/FireWorks/). This repo is a start at building a more sustainable path towards sharing of code examples. 

It is not limited to the codes we develop - any use of open source software for materials analysis is welcome. Also, anyone is welcome to contribute. 

Just fork, write your awesome notebook and submit a pull request.

# How to contribute

1. Fork this repo and clone.
2. Write a new notebook in the `notebooks` folder.
3. Notebooks should be well-documented and simple. The idea here is to be pedagogical. A newcomer to the software (with the right materials science background) should be able to follow the logic without too much difficulty. Feel free to add authorship and contact information, as well as works to cite and acknowledge your contributions.
4. Notebooks should be placed in the `notebooks` folder, and the name should start with the date in `YYYY-MM-DD-<intuitive title>`format. See [existing examples](https://github.com/materialsvirtuallab/matgenb/tree/master/notebooks).
5. In the root folder of the repo, type `jupyter nbconvert --to html notebooks/*.ipynb --output-dir docs/_posts`
5. Commit, push and submit a pull request.

# Search

<form action="/search.html" method="get">
  <label for="search-box">Search</label>
  <input type="text" id="search-box" name="query">
  <input type="submit" value="search">
</form>