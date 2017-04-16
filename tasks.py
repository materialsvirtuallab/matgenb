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
def update_html(ctx):

    year = str(datetime.datetime.now().year)
    with cd(year):
        ctx.run("jupyter nbconvert --to html *.ipynb")
    
    toc = defaultdict(list)
    for f in glob.glob("*/*.html"):
        year, html = f.split("/")
        toc[year].append('<a href="%s">%s</a>' % (f, html))
    
    output = []
    for k in sorted(toc.keys(), reverse=True):
        output.append('<h1>%s</h1>' % k)
        output.append('<ul>')
        docs = toc[k]
        docs.reverse()
        for d in toc[k]:
            output.append('<li>%s</li>' % d)
        output.append('</ul>')

    with open("toc.html", "wt") as f:
        f.write("\n".join(output))
