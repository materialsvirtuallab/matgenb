Visit the [Github Pages](http://matgenb.materialsvirtuallab.org) for a nicely formatted HTML page and notebook search functionality.

# Introduction

This repo is started by the [Materials Virtual Lab](http://www.materialsvirtuallab.org) as a useful collection of
Jupyter notebooks that demonstrate the utilization of open-source codes for the study of materials science.

We frequently get requests (from students, postdocs, collaborators, or just general users) for example codes that
demonstrate various capabilities in the open-source software we maintain and contribute to, such as the Materials
Project software stack comprising [Python Materials Genomics (pymatgen)](http://www.pymatgen.org),
[Custodian](https://materialsprojecthub.io/custodian/), and [Fireworks](https://pythonhosted.org/FireWorks/). This
repo is a start at building a more sustainable path towards sharing of code examples.

It is not limited to the codes we develop - any use of open source software for materials analysis is welcome. Also,
anyone is welcome to contribute.

# Running the examples from a browser

## Option 1: Google Colab

You can easily run all the notebooks via [Google Colab](https://colab.research.google.com/).

## Option 2: BinderHub

One of the best ways to get a feel of the functionality is to run it yourself using BinderHub. Click on the icon below
to start a BinderHub instance where you can explore the notebooks, make any changes to the code to see the changes in
output.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/materialsvirtuallab/matgenb/master)

# Contributing

1. Fork this repo and clone.

    ```sh
    git clone git@github.com:<your_github_username>/matgenb
    cd matgenb
    ```

2. Write a new notebook in the `notebooks` folder.

    ```sh
    cd notebooks
    jupyter notebook
    ```

3. Notebooks should be well-documented and simple. The idea here is to be pedagogical. A newcomer to the software
   (with the right materials science background) should be able to follow the logic without too much difficulty. Feel
   free to add authorship and contact information, as well as works to cite and acknowledge your contributions. In view
   that scientific codes tend to be continuously being updated, please put in a list of the key pinned dependencies so
   that other users can install the exact version of software to run the notebook if needed. The best practice is to put
   a section that provides a commented out pip install instructure that can be used in Google Colab. For example,
   ```sh
   # Uncomment the subsequent lines in this cell to install dependencies for Google Colab.
   # !pip install -U pymatgen
   ```

4. Ideally, please update notebooks as needed to use more modern versions of the codes, and you may update the date of
   the notebook as needed.

5. Notebooks should be placed in the `notebooks` folder, and the name should start with the date in
   `YYYY-MM-DD-<intuitive title>` format. See [existing examples](https://github.com/materialsvirtuallab/matgenb/tree/master/notebooks).

6. In the root folder of the repo, convert the jupyter notebooks to html.

    ```sh
    jupyter nbconvert --to html notebooks/*.ipynb --output-dir docs/_posts
    ```

7. Commit and push.

    ```sh
    git add .
    git commit -a -m "Describe your contribution"
    git push
    ```

8. Submit a pull request from Github.
