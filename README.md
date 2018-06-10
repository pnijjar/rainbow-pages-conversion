Rainbow Pages Conversion Scripts
================================

This is a skunkworks script to convert a spreadsheet of Rainbow LBGTQ+
resources into an HTML page, as an intermediate step towards creating
a printed calendar. 

Setup
-----

You will need `python3`. You probably want `virtualenv`. This was
tested on Debian; your kilometerage may vary. 

- `virtualenv -p /usr/bin/python3 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt` 
- Edit the `rainbow-csv-to-html.py` script to point to your CSV file.
- Run `rainbow-csv-to-html.py > rainbow-pages.html`


Conversion Workflow
-------------------

You will need `pandoc` and something that can read Excel spreadsheet
for this (LibreOffice worked for me)

- Take the Excel spreadsheet and save a copy in CSV format. Unicode
  output is okay.
- Run this script to turn it into HTML.
- Run `pandoc -o rainbow-pages.docx rainbow-pages.html` to convert the
  HTML into Microsoft Word format.
- Hand the .docx file to somebody who will import it into Microsoft
  Publisher
- Profit?
