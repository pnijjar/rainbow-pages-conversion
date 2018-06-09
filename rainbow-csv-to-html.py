#!/usr/bin/env python3

""" 
Convert a CSV file of Rainbow information to an HTML file, which
can then be pandoc'ed into a Word file, which can then be imported
into Publisher. Oy vey.

Paul "Worthless" Nijjar, 2018-06-08
"""

import csv
import jinja2

SRC="2018-05SPECTRUM-DirDataStructureRevision.csv"
HTML_TEMPLATE="rainbow-entry.jinja"
TEMPLATE_DIR="."

with open(SRC) as rainbow_csv:
    reader = csv.DictReader(rainbow_csv)

    #for row in reader:
    #    print(row['CompanyOrgName'], row['Web'])

    template_loader = jinja2.FileSystemLoader(
        searchpath=TEMPLATE_DIR,
        )
    template_env = jinja2.Environment(
        loader=template_loader,
        lstrip_blocks=True,
        trim_blocks=True,
        )

    template = template_env.get_template( HTML_TEMPLATE )

    template_vars = {
      "category": "Moo cow",
      "rainbow_items" : reader,
      }

    output_html = template.render(template_vars)
    print(output_html)





