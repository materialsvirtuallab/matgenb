from datetime import datetime

from invoke import task

"""
Deployment file to facilitate generation of doc.
"""

__author__ = "Shyue Ping Ong"
__email__ = "ongsp@ucsd.edu"
__date__ = "Sep 1, 2014"


@task
def update_html(ctx, year: str = None):
    year = year or f"{datetime.now():%Y}"
    ctx.run(f"rm docs/_posts/{year}-*.html")
    ctx.run(
        f"jupyter nbconvert --to html notebooks/{year}-*.ipynb --output-dir "
        "docs/_posts"
    )
