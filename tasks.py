# coding: utf-8

import glob
import os
from invoke import task
import datetime
from monty.os import cd
from collections import defaultdict


"""
Deployment file to facilitate generation of doc.
"""

__author__ = "Shyue Ping Ong"
__email__ = "ongsp@ucsd.edu"
__date__ = "Sep 1, 2014"


@task
def update_html(ctx, year=str(datetime.datetime.now().year)):
    ctx.run("rm docs/_posts/%s-*.html" % year)
    ctx.run("jupyter nbconvert --to html notebooks/%s-*.ipynb --output-dir docs/_posts" % year)
