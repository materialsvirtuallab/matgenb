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
    with cd("notebooks"):
        ctx.run("jupyter nbconvert --to html *.ipynb")
        ctx.run("mv *.html ../docs/_posts")

    # with cd("docs"):
    #     toc = defaultdict(list)
    #     for f in glob.glob("*/*.html"):
    #         year, title = f.split("/")
    #         toc[year].append((title, f))
        
    #     output = []
    #     for k in sorted(toc.keys(), reverse=True):
    #         output.append('## %s' % k)
    #         output.append('')
    #         docs = toc[k]
    #         docs.reverse()
    #         for d in toc[k]:
    #             output.append('* [%s](%s)' % d)
    #         output.append('')

    #     with open("README.template") as f:
    #         contents = f.read()
    #         output = contents.format(TOC="\n".join(output))

    #     with open("README.md", "wt") as f:
    #         f.write(output)
