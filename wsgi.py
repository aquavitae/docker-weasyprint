#!/usr/bin/env python

from flask import Flask, request
from weasyprint import HTML

app = Flask('pdf')


@app.route('/<name>', methods=['POST'])
def generate(name='unnamed'):
    html = HTML(string=request.data)
    pdf = html.write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % name
    return response


if __name__ == '__main__':
    app.run()
