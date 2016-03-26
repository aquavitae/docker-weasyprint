# docker-weasyprint

[![Build Status](https://travis-ci.org/aquavitae/docker-weasyprint.svg?branch=master)](https://travis-ci.org/aquavitae/docker-weasyprint)

[Weasyprint](http://weasyprint.org/) as a microservice in a docker image.

# Usage

Run the docker image, exposing port 5001

```
docker run -p 5001:5001 aquavitae/weasyprint
```

A `POST` to port 5001 with an html body with give a response containing a PDF. The POST path gives the filename that will be used in the response header.  E.g.:

```
curl -X POST -d @source.html http://127.0.0.1:5001/result
```

This will use the file `source.html` and return a response with `Content-Type: application/pdf` and `Content-Disposition: inline; filename=result.pdf` headers.  The body of the response will be the PDF.

In addition `/health` is a health check endpoint and a `GET` returns 'ok'.
